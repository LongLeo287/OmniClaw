//! Risk classification for generated changes.
//!
//! Classifies each contribution as LOW/MEDIUM/HIGH risk
//! to control auto-submission behavior.

use std::fmt;

/// Risk level for a generated change.
#[derive(Debug, Clone, Copy, PartialEq, Eq, PartialOrd, Ord)]
pub enum RiskLevel {
    /// Docs, comments, typos, formatting — safe to auto-submit.
    Low,
    /// Bug fixes, imports, naming — submit with review note.
    Medium,
    /// Multi-file refactors, behavior changes — require approval.
    High,
}

impl fmt::Display for RiskLevel {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            RiskLevel::Low => write!(f, "LOW"),
            RiskLevel::Medium => write!(f, "MEDIUM"),
            RiskLevel::High => write!(f, "HIGH"),
        }
    }
}

/// Result of risk classification.
#[derive(Debug, Clone)]
pub struct RiskClassification {
    pub level: RiskLevel,
    pub reason: String,
    pub auto_submit: bool,
}

/// Classify the risk level of a generated contribution.
///
/// # Arguments
/// * `change_type` - The type of change (e.g., "docs", "security_fix", "refactor")
/// * `files_changed` - List of files being modified
/// * `diff_lines` - Approximate number of lines changed
pub fn classify_risk(
    change_type: &str,
    files_changed: &[String],
    diff_lines: usize,
) -> RiskClassification {
    let change_lower = change_type.to_lowercase();
    let file_count = files_changed.len();

    // Rule 1: Docs, comments, typos → LOW
    if matches!(
        change_lower.as_str(),
        "docs" | "documentation" | "typo" | "comment" | "readme" | "docstring"
    ) {
        return RiskClassification {
            level: RiskLevel::Low,
            reason: format!("Documentation change ({})", change_type),
            auto_submit: true,
        };
    }

    // Rule 2: Formatting, imports, naming → LOW
    if matches!(
        change_lower.as_str(),
        "formatting" | "style" | "import" | "naming" | "lint" | "whitespace"
    ) {
        return RiskClassification {
            level: RiskLevel::Low,
            reason: format!("Style/formatting change ({})", change_type),
            auto_submit: true,
        };
    }

    // Rule 3: Multi-file changes (3+) or large diffs (100+ lines) → HIGH
    if file_count >= 3 || diff_lines >= 100 {
        return RiskClassification {
            level: RiskLevel::High,
            reason: format!("Large change: {} files, ~{} lines", file_count, diff_lines),
            auto_submit: false,
        };
    }

    // Rule 4: Security fixes → MEDIUM (important but needs care)
    if matches!(
        change_lower.as_str(),
        "security" | "security_fix" | "vulnerability" | "xss" | "sqli" | "injection"
    ) {
        return RiskClassification {
            level: RiskLevel::Medium,
            reason: format!("Security fix ({})", change_type),
            auto_submit: true,
        };
    }

    // Rule 5: Behavior changes, refactors → HIGH
    if matches!(
        change_lower.as_str(),
        "refactor" | "behavior" | "breaking" | "api_change" | "architecture"
    ) {
        return RiskClassification {
            level: RiskLevel::High,
            reason: format!("Behavior/structural change ({})", change_type),
            auto_submit: false,
        };
    }

    // Rule 6: Small single-file bug fixes → MEDIUM
    if file_count <= 1 && diff_lines <= 30 {
        return RiskClassification {
            level: RiskLevel::Medium,
            reason: format!("Small fix: {} file, ~{} lines", file_count, diff_lines),
            auto_submit: true,
        };
    }

    // Default: MEDIUM
    RiskClassification {
        level: RiskLevel::Medium,
        reason: format!(
            "Code change: {} ({} files, ~{} lines)",
            change_type, file_count, diff_lines
        ),
        auto_submit: true,
    }
}

/// Check if a risk level is allowed given a tolerance setting.
///
/// * `"low"` — only LOW risk changes auto-submit
/// * `"medium"` — LOW + MEDIUM (default)
/// * `"high"` — everything auto-submits
pub fn is_within_tolerance(level: RiskLevel, tolerance: &str) -> bool {
    match tolerance {
        "low" => level == RiskLevel::Low,
        "high" => true,
        _ => level <= RiskLevel::Medium, // "medium" default
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_docs_are_low_risk() {
        let r = classify_risk("docs", &["README.md".into()], 10);
        assert_eq!(r.level, RiskLevel::Low);
        assert!(r.auto_submit);
    }

    #[test]
    fn test_formatting_is_low_risk() {
        let r = classify_risk("formatting", &["src/main.rs".into()], 5);
        assert_eq!(r.level, RiskLevel::Low);
        assert!(r.auto_submit);
    }

    #[test]
    fn test_security_fix_is_medium() {
        let r = classify_risk("security_fix", &["src/auth.rs".into()], 15);
        assert_eq!(r.level, RiskLevel::Medium);
        assert!(r.auto_submit);
    }

    #[test]
    fn test_large_change_is_high_risk() {
        let files: Vec<String> = (0..5).map(|i| format!("file{}.rs", i)).collect();
        let r = classify_risk("code_quality", &files, 200);
        assert_eq!(r.level, RiskLevel::High);
        assert!(!r.auto_submit);
    }

    #[test]
    fn test_refactor_is_high_risk() {
        let r = classify_risk("refactor", &["src/main.rs".into()], 50);
        assert_eq!(r.level, RiskLevel::High);
        assert!(!r.auto_submit);
    }

    #[test]
    fn test_small_fix_is_medium() {
        let r = classify_risk("bug_fix", &["src/lib.rs".into()], 10);
        assert_eq!(r.level, RiskLevel::Medium);
        assert!(r.auto_submit);
    }

    #[test]
    fn test_tolerance_low() {
        assert!(is_within_tolerance(RiskLevel::Low, "low"));
        assert!(!is_within_tolerance(RiskLevel::Medium, "low"));
        assert!(!is_within_tolerance(RiskLevel::High, "low"));
    }

    #[test]
    fn test_tolerance_medium() {
        assert!(is_within_tolerance(RiskLevel::Low, "medium"));
        assert!(is_within_tolerance(RiskLevel::Medium, "medium"));
        assert!(!is_within_tolerance(RiskLevel::High, "medium"));
    }

    #[test]
    fn test_tolerance_high() {
        assert!(is_within_tolerance(RiskLevel::Low, "high"));
        assert!(is_within_tolerance(RiskLevel::Medium, "high"));
        assert!(is_within_tolerance(RiskLevel::High, "high"));
    }

    #[test]
    fn test_risk_display() {
        assert_eq!(format!("{}", RiskLevel::Low), "LOW");
        assert_eq!(format!("{}", RiskLevel::Medium), "MEDIUM");
        assert_eq!(format!("{}", RiskLevel::High), "HIGH");
    }

    #[test]
    fn test_risk_ordering() {
        assert!(RiskLevel::Low < RiskLevel::Medium);
        assert!(RiskLevel::Medium < RiskLevel::High);
    }
}
