---
id: github.com-paradedb-pg-schema-diff-b8d32d17-knowle
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:10.948505
---

# KNOWLEDGE EXTRACT: github.com_paradedb_pg-schema-diff_b8d32d17
> **Extracted on:** 2026-04-01 15:09:36
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524319/github.com_paradedb_pg-schema-diff_b8d32d17

---

## File: `.gitignore`
```
/target
/a.sql
/b.sql
/foo.sql
.idea/
.*.swp
```

## File: `.licensure.yml`
```yaml
excludes:
  - \.gitignore
  - .*lock
  - \.git/.*
  - \.licensure\.yml
  - README.*
  - LICENSE.*
  - .*\.(md|rst|txt)

licenses:
  - files: rs
    ident: Postgres
    authors:
      - name: Eric B. Ridge
        email: eebbrr@gmail.com
    template: |
      Copyright 2020-[year] [name of author]. All rights reserved. Use of
      this source code is governed by the [ident] license that can be
      found in the LICENSE file.

comments:
  - extension: rs
    columns: 80
    commenter:
      type: line
      comment_char: "//"
      trailing_lines: 0

```

## File: `Cargo.toml`
```
[package]
name = "pg-schema-diff"
version = "0.0.1"
authors = ["Eric B. Ridge <eebbrr@gmail.com>"]
edition = "2021"
license = "LICENSE"

[dependencies]
colored = "2.0.0"
indexmap = "2.5.0"
postgres-parser = "*"
rand = "0.8.3"
```

## File: `LICENSE`
```
pg-schema-diff

Copyright (c) 2020-2026, Eric B. Ridge (eebbrr@gmail.com)

Permission to use, copy, modify, and distribute this software and its documentation for any purpose, without fee,and without a written agreement is hereby granted, provided that the above copyright notice and this paragraph and the following two paragraphs appear in all copies.

IN NO EVENT SHALL Eric B. Ridge BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING LOST PROFITS, ARISING OUT OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION, EVEN IF Eric B.Ridge HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Eric B. Ridge SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF 
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE SOFTWARE PROVIDED HEREUNDER IS ON AN "AS IS" BASIS, ANDEric B. Ridge HAS NO OBLIGATIONS TO PROVIDE MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.
```

## File: `src/main.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{SchemaSet, Sql, SqlIdent};
use postgres_parser::*;

mod nodes;
mod schema_set;

static EMPTY_NODE_VEC: Vec<Node> = Vec::new();

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let command = args.get(1).expect("no command argument");

    match command.as_str() {
        "deparse" => {
            let filename = args.get(2).expect("noo filename argument");
            let mut set = SchemaSet::new();
            set.scan_file(&filename);
            let deparsed = set.deparse();
            println!("{}", deparsed);
        }

        "diff" => {
            let a = args.get(2).expect("no a filename");
            let b = args.get(3).expect("no b filename");

            let mut a_set = SchemaSet::new();
            let mut b_set = SchemaSet::new();

            a_set.scan_file(&a);
            b_set.scan_file(&b);

            let differences = a_set.diff(&b_set);
            println!("{}", differences);
        }

        unknown => panic!("unrecognized command argument: {}", unknown),
    }
}

pub fn make_individual_names(names: &Option<Vec<Node>>) -> Vec<String> {
    let mut result = Vec::new();

    if names.is_some() {
        for name in names.as_ref().unwrap() {
            result.push(
                make_name(&Some(vec![name.clone()])).expect("failed to make an individual name"),
            );
        }
    }

    result
}

pub fn make_name(names: &Option<Vec<Node>>) -> Result<String, PgParserError> {
    match names {
        Some(names) => {
            let mut result = String::new();
            for name in names {
                if !result.is_empty() {
                    result.push('.');
                }

                match name {
                    crate::Node::Value(value) if value.string.is_some() => {
                        // let ident = value.string.sql_ident();
                        // if &ident != "pg_catalog" {
                            result.push_str(&value.string.sql_ident());
                        // }
                    }
                    crate::Node::A_Star(a_star) => {
                        result.push_str(&a_star.sql());
                    }
                    _ => return Err(PgParserError::NotAString),
                }
            }
            Ok(result)
        }

        // None => Err(PgParserError::InternalNull),
        None => Ok("".into()),
    }
}

pub fn make_operator_name(names: &Option<Vec<Node>>) -> Result<String, PgParserError> {
    match names {
        Some(names) => {
            if names.len() == 1 {
                return Ok(names[0].sql());
            }

            let mut result = String::new();
            result.push_str("OPERATOR(");
            let mut iter = names.iter().enumerate().peekable();
            while let Some((i, name)) = iter.next() {
                if i > 0 {
                    result.push('.');
                }

                match name {
                    crate::Node::Value(value) if value.string.is_some() => {
                        if iter.peek().is_none() {
                            // don't quote the operator itself
                            result.push_str(&value.string.as_ref().unwrap());
                        } else {
                            result.push_str(&value.string.sql_ident());
                        }
                    }
                    crate::Node::A_Star(a_star) => {
                        result.push_str(&a_star.sql());
                    }
                    _ => return Err(PgParserError::NotAString),
                }
            }
            result.push(')');
            Ok(result)
        }

        None => Err(PgParserError::InternalNull),
    }
}

pub fn get_string_value(node: &Node) -> &Option<String> {
    if let Node::Value(value) = node {
        return &value.string;
    }
    return &None;
}

pub fn get_float_value(node: &Node) -> &Option<String> {
    if let Node::Value(value) = node {
        return &value.float;
    }
    return &None;
}

pub fn get_int_value(node: &Node) -> &Option<i32> {
    if let Node::Value(value) = node {
        return &value.int;
    }
    return &None;
}

pub fn get_bool_value(node: &Node) -> bool {
    if let Node::Value(value) = node {
        return value.int == Some(1);
    }
    return false;
}
```

## File: `src/schema_set.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::{make_name, EMPTY_NODE_VEC};
use postgres_parser::{parse_query, quote_identifier, Node, SqlStatementScanner};

use colored::Colorize;
use std::borrow::Cow;

use std::fmt::Debug;
use std::hash::{Hash, Hasher};
use std::panic::{catch_unwind, RefUnwindSafe};

#[derive(Debug)]
pub struct DiffableStatement {
    tree_string: String,
    sql: String,
    node: Node,
    differ: Box<dyn Diff>,
}

impl Hash for DiffableStatement {
    fn hash<H: Hasher>(&self, state: &mut H) {
        self.differ.identifier(&self.tree_string).hash(state)
    }
}

impl Eq for DiffableStatement {}
impl PartialEq for DiffableStatement {
    fn eq(&self, other: &Self) -> bool {
        self.differ
            .identifier(&self.tree_string)
            .eq(&other.differ.identifier(&other.tree_string))
    }
}

impl RefUnwindSafe for DiffableStatement {}

impl DiffableStatement {
    fn new(sql: &str, node: Node, differ: impl Diff + 'static) -> Self {
        let mut sql = sql.trim();
        if sql.ends_with(';') {
            sql = &sql[..sql.len() - 1];
        }
        DiffableStatement {
            tree_string: format!("{:?}", node),
            sql: sql.trim().into(),
            node,
            differ: Box::new(differ),
        }
    }
}

pub trait Diff: Sql + Debug {
    fn alter_stmt(&self, _other: &Node) -> Option<String> {
        println!(
            "/*\nDon't know how to ALTER:\n{}\n{:?}\n{:?}\n*/",
            self.sql(),
            _other,
            self
        );
        return None;
    }

    fn drop_stmt(&self) -> Option<String> {
        unimplemented!("Don't know how to drop: {:#?}", self)
    }

    fn object_name(&self) -> Option<String> {
        None
    }

    fn object_type(&self) -> String {
        String::new()
    }

    fn identifier<'a>(&self, tree_string: &'a str) -> Cow<'a, str> {
        match self.object_name() {
            Some(name) => Cow::Owned(name + &self.object_type()),
            None => Cow::Borrowed(tree_string),
        }
    }
}

pub trait SqlMaybeList {
    fn sql_maybe_list(&self, sep: &str) -> String;
}

impl SqlMaybeList for Option<Box<Node>> {
    fn sql_maybe_list(&self, sep: &str) -> String {
        match self {
            None => String::new(),
            Some(boxed_sql) => boxed_sql.sql_maybe_list(sep),
        }
    }
}

impl SqlMaybeList for Node {
    fn sql_maybe_list(&self, sep: &str) -> String {
        if let Node::List(v) = self {
            v.sql(sep)
        } else {
            self.sql()
        }
    }
}

pub trait Sql {
    fn sql_prefix(&self, pre: &str) -> String {
        format!("{}{}", pre, self.sql())
    }
    #[track_caller]
    fn sql_wrap(&self, pre: &str, post: &str) -> String {
        format!("{}{}{}", pre, self.sql(), post)
    }
    fn sql_prefix_and_wrap(&self, pre: &str, start: &str, end: &str) -> String {
        format!("{}{}{}{}", pre, start, self.sql(), end)
    }
    fn sql(&self) -> String;
}

pub trait SqlList {
    fn sql(&self, sep: &str) -> String;
    fn sql_prefix(&self, pre: &str, sep: &str) -> String;
    fn sql_prefix_and_wrap(&self, pre: &str, start: &str, end: &str, sep: &str) -> String;
    fn sql_wrap_each(&self, pre: Option<&str>, post: Option<&str>) -> String;
    fn sql_wrap_each_and_separate(&self, sep: &str, pre: &str, post: &str) -> String;
    fn sql_wrap(&self, sep: &str, pre: &str, post: &str) -> String;
}

pub trait SqlIdent {
    fn sql_ident(&self) -> String;
    fn sql_ident_prefix(&self, pre: &str) -> String;
    fn sql_ident_suffix(&self, suf: &str) -> String;
}

pub trait SqlCollect {
    fn sql_wrap(self, pre: &str, post: &str) -> String;
    fn sql(self) -> String;
}

impl<T: Sql> Sql for Option<Box<T>> {
    fn sql_prefix(&self, pre: &str) -> String {
        match self {
            None => String::new(),
            Some(boxed_sql) => format!("{}{}", pre, boxed_sql.sql()),
        }
    }

    fn sql_wrap(&self, pre: &str, post: &str) -> String {
        match self {
            None => String::new(),
            Some(boxed_sql) => boxed_sql.sql_wrap(pre, post),
        }
    }

    fn sql_prefix_and_wrap(&self, pre: &str, start: &str, end: &str) -> String {
        match self {
            None => String::new(),
            Some(boxed_sql) => format!("{}{}{}{}", pre, start, boxed_sql.sql(), end),
        }
    }

    #[track_caller]
    fn sql(&self) -> String {
        match self {
            None => String::new(),
            Some(boxed_sql) => boxed_sql.sql(),
        }
    }
}

impl SqlIdent for Option<String> {
    fn sql_ident(&self) -> String {
        quote_identifier(self)
    }

    fn sql_ident_prefix(&self, pre: &str) -> String {
        match self {
            None => String::new(),
            Some(_) => format!("{}{}", pre, self.sql_ident()),
        }
    }

    fn sql_ident_suffix(&self, suf: &str) -> String {
        match self {
            None => String::new(),
            Some(_) => format!("{}{}", self.sql_ident(), suf),
        }
    }
}

impl SqlIdent for Option<Vec<Node>> {
    #[track_caller]
    fn sql_ident(&self) -> String {
        make_name(self).expect("unable to make SqlIdent")
    }

    #[track_caller]
    fn sql_ident_prefix(&self, pre: &str) -> String {
        match self {
            None => String::new(),
            Some(_) => format!("{}{}", pre, self.sql_ident()),
        }
    }

    #[track_caller]
    fn sql_ident_suffix(&self, suf: &str) -> String {
        match self {
            None => String::new(),
            Some(_) => format!("{}{}", self.sql_ident(), suf),
        }
    }
}

impl SqlIdent for Vec<Node> {
    #[track_caller]
    fn sql_ident(&self) -> String {
        make_name(&Some(self.clone())).expect("unable to make SqlIdent")
    }

    #[track_caller]
    fn sql_ident_prefix(&self, pre: &str) -> String {
        format!("{}{}", pre, self.sql_ident())
    }

    #[track_caller]
    fn sql_ident_suffix(&self, suf: &str) -> String {
        format!("{}{}", self.sql_ident(), suf)
    }
}

impl SqlIdent for Option<Box<Node>> {
    #[track_caller]
    fn sql_ident(&self) -> String {
        match self {
            None => String::new(),
            Some(node) => {
                make_name(&Some(vec![node.as_ref().clone()])).expect("unable to make SqlIdent")
            }
        }
    }

    #[track_caller]
    fn sql_ident_prefix(&self, pre: &str) -> String {
        match self {
            None => String::new(),
            Some(_) => format!("{}{}", pre, self.sql_ident()),
        }
    }

    #[track_caller]
    fn sql_ident_suffix(&self, suf: &str) -> String {
        match self {
            None => String::new(),
            Some(_) => format!("{}{}", self.sql_ident(), suf),
        }
    }
}

impl SqlIdent for Node {
    #[track_caller]
    fn sql_ident(&self) -> String {
        make_name(&Some(vec![self.clone()])).expect("unable to make SqlIdent")
    }

    #[track_caller]
    fn sql_ident_prefix(&self, pre: &str) -> String {
        format!("{}{}", pre, self.sql_ident())
    }

    #[track_caller]
    fn sql_ident_suffix(&self, suf: &str) -> String {
        format!("{}{}", suf, self.sql_ident())
    }
}

pub trait Len {
    fn len(&self) -> usize;
    fn is_empty(&self) -> bool {
        self.len() == 0
    }
}

impl Len for Option<Vec<Node>> {
    fn len(&self) -> usize {
        self.as_ref().unwrap_or(&EMPTY_NODE_VEC).len()
    }
}

#[derive(Debug)]
pub struct SchemaSet {
    nodes: indexmap::IndexSet<DiffableStatement>,
}

impl Default for SchemaSet {
    fn default() -> Self {
        SchemaSet {
            nodes: Default::default(),
        }
    }
}

impl SchemaSet {
    pub fn new() -> Self {
        Default::default()
    }

    pub fn push(&mut self, sql: &str, node: Node) {
        #[inline]
        fn push(
            nodes: &mut indexmap::IndexSet<DiffableStatement>,
            sql: &str,
            node: Node,
            differ: impl Diff + 'static,
        ) {
            nodes.insert(DiffableStatement::new(sql, node, differ));
        }

        match node.clone() {
            Node::AlterCollationStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::AlterFunctionStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::AlterObjectSchemaStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::AlterOwnerStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::AlterTableStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::AlterTypeStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::ClusterStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::CommentStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::CompositeTypeStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::CopyStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::CreateAmStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::CreateCastStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::CreateConversionStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::CreateDomainStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::CreateEnumStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::CreateForeignServerStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::CreateForeignTableStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::CreateFdwStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::CreateFunctionStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::CreateOpClassStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::CreatePolicyStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::CreateRangeStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::CreateRoleStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::CreateSeqStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::CreateSchemaStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::CreateStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::CreateTableAsStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::CreateTrigStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::DeclareCursorStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::DefineStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::DeleteStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::DiscardStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::DoStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::DropRoleStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::DropStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::ExplainStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::FetchStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::GrantRoleStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::GrantStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::IndexStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::InsertStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::ListenStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::LockStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::NotifyStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::PrepareStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::RenameStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::RuleStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::SelectStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::TransactionStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::TruncateStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::UnlistenStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::UpdateStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::VacuumStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::VariableSetStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::VariableShowStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::ViewStmt(stmt) => push(&mut self.nodes, sql, node, stmt),
            Node::CreateEventTrigStmt(stmt) => push(&mut self.nodes, sql, node, stmt),

            _ => println!("/*\nunknown node: {:?}\n\n{}\n*/", node, sql),
        };
    }

    pub fn scan_file(&mut self, filename: &str) {
        let mut sql =
            std::fs::read_to_string(filename).expect(&format!("failed to read file: {}", filename));
        sql = sql.replace("@extschema@", "\"@extschema@\"");
        let scanner = SqlStatementScanner::new(&sql);
        for stmt in scanner.into_iter() {
            match stmt.parsetree {
                Ok(parsetree) => {
                    if let Some(node) = parsetree {
                        self.push(stmt.sql, node);
                    }
                }

                // it couldn't be parsed -- panic!
                Err(e) => {
                    panic!("INPUT PARSE ERROR: {:?}\n{}\n/---", e, stmt.sql.trim());
                }
            };
        }
    }

    pub fn deparse(&self) -> String {
        let mut sql = String::new();

        for node in &self.nodes {
            if let Node::AlterTableStmt(_) = &node.node {
                println!("skipping AlterTableStmt");
                continue;
            }
            // println!("{}", node.sql);
            let deparsed = match catch_unwind(|| node.node.sql()) {
                Ok(deparsed) => deparsed,
                Err(e) => {
                    panic!(
                        "{:?}\n\n\nnode=\n{:#?}\nsql={}",
                        e,
                        node.node,
                        node.sql.trim(),
                    )
                }
            };
            let reparsed = parse_query(&deparsed).unwrap_or_else(|e| {
                panic!(
                    "FAILED TO REPARSE:\n{:#?}\n{:#?}\nORIG:\n   {}\nNEW:\n   {};",
                    e, node.node, node.sql, deparsed,
                )
            });
            if &node.node != reparsed.get(0).expect("didn't parse anything") {
                panic!(
                    "TREES NOT EQUAL:{:#?};\n---------\n{:#?};\n\n\nORIG:\n   {}\nNEW:\n   {};\n",
                    node.node,
                    reparsed.get(0).unwrap(),
                    node.sql,
                    deparsed
                );
            }

            sql.push_str("==================\n");
            sql.push_str(&format!("{}:\n{}\n", "BEFORE".yellow(), node.sql.trim()));
            sql.push_str(&format!("{}:\n{};\n", "AFTER".green(), deparsed.trim()));
            sql.push_str("/=================\n");
        }

        sql
    }

    pub fn diff(self, that: &SchemaSet) -> String {
        let mut sql = String::new();

        // Find objects in 'self' that don't exist in 'that' so we can DROP them
        for this_node in &self.nodes {
            if !that.nodes.contains(this_node) {
                match this_node.differ.drop_stmt() {
                    Some(drop) => {
                        sql.push_str(&drop);
                        sql.push_str(";\n");
                    }
                    None => {
                        // it's a statement that we don't know how to drop
                    }
                }
            }
        }

        // find objects that are either in both or only in 'that'
        for that_node in &that.nodes {
            // do we have that_node?
            match self.nodes.get(that_node) {
                // yes, we do have that node, so lets see if it's different
                Some(this_node) => {
                    if &this_node.node.sql() != &that_node.node.sql() {
                        // they are different, so we try to alter it
                        if let Some(alter) = this_node.differ.alter_stmt(&that_node.node) {
                            sql.push_str(&alter);
                            sql.push_str(";\n");
                        }
                    }
                }

                // no, we don't have that node, so we need to just its sql directly
                None => {
                    sql.push_str(&that_node.sql);
                    sql.push_str(";\n");
                }
            }
        }

        sql
    }
}
```

## File: `src/nodes/a_arrayexpr.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlList};

use postgres_parser::nodes::A_ArrayExpr;

impl Sql for A_ArrayExpr {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("ARRAY[");
        sql.push_str(&self.elements.sql(", "));
        sql.push(']');

        sql
    }
}
```

## File: `src/nodes/a_const.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::Sql;
use postgres_parser::nodes::A_Const;

impl Sql for A_Const {
    fn sql(&self) -> String {
        let mut sql = String::new();

        if let Some(i) = self.val.int.as_ref() {
            sql.push_str(&i.to_string());
        } else if let Some(s) = self.val.string.as_ref() {
            sql.push('\'');
            sql.push_str(&s.replace('\'', "''"));
            sql.push('\'');
        } else if let Some(_) = self.val.null.as_ref() {
            sql.push_str("NULL");
        } else if let Some(f) = self.val.float.as_ref() {
            sql.push_str(f);
        } else if let Some(b) = self.val.bit_string.as_ref() {
            let bitstring = &b[1..];
            sql.push('B');
            sql.push('\'');
            sql.push_str(bitstring);
            sql.push('\'');
        }

        sql
    }
}
```

## File: `src/nodes/a_expr.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::make_operator_name;
use crate::schema_set::{Sql, SqlList, SqlMaybeList};
use postgres_parser::nodes::A_Expr;
use postgres_parser::sys::A_Expr_Kind;
use postgres_parser::Node;

impl Sql for A_Expr {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push('(');
        match self.kind {
            A_Expr_Kind::AEXPR_OP => {
                sql.push_str(&self.lexpr.sql());
                sql.push(' ');
                sql.push_str(
                    &make_operator_name(&self.name).expect("failed to make AEXPR_OP for A_Expr"),
                );
                sql.push(' ');
                sql.push_str(&self.rexpr.sql());
            }
            A_Expr_Kind::AEXPR_OP_ANY => {
                sql.push_str(&self.lexpr.sql());
                sql.push(' ');
                sql.push_str(
                    &make_operator_name(&self.name).expect("failed to make AEXPR_ALL for A_Expr"),
                );
                sql.push_str(&self.rexpr.sql_wrap(" ANY (", ")"));
            }
            A_Expr_Kind::AEXPR_OP_ALL => {
                sql.push_str(&self.lexpr.sql());
                sql.push(' ');
                sql.push_str(
                    &make_operator_name(&self.name).expect("failed to make AEXPR_ALL for A_Expr"),
                );
                sql.push_str(&self.rexpr.sql_wrap(" ALL (", ")"));
            }
            A_Expr_Kind::AEXPR_DISTINCT => {
                sql.push_str(&self.lexpr.sql());
                sql.push_str(" IS DISTINCT FROM ");
                sql.push_str(&self.rexpr.sql());
            }
            A_Expr_Kind::AEXPR_NOT_DISTINCT => {
                sql.push_str(&self.lexpr.sql());
                sql.push_str(" IS NOT DISTINCT FROM ");
                sql.push_str(&self.rexpr.sql());
            }
            A_Expr_Kind::AEXPR_NULLIF => {
                sql.push_str(" NULLIF (");
                sql.push_str(&self.lexpr.sql());
                sql.push_str(", ");
                sql.push_str(&self.rexpr.sql());
                sql.push(')');
            }
            A_Expr_Kind::AEXPR_OF => {
                sql.push_str(&self.lexpr.sql());
                sql.push_str(" IS OF (");
                sql.push_str(&self.rexpr.sql_maybe_list(", "));
                sql.push(')');
            }
            A_Expr_Kind::AEXPR_IN => {
                sql.push_str(&self.lexpr.sql());
                sql.push_str(" IN (");
                sql.push_str(&self.rexpr.sql_maybe_list(", "));
                sql.push(')');
            }
            A_Expr_Kind::AEXPR_LIKE => {
                sql.push_str(&self.lexpr.sql());
                sql.push_str(" LIKE ");
                sql.push_str(&self.rexpr.sql());
            }
            A_Expr_Kind::AEXPR_ILIKE => {
                sql.push_str(&self.lexpr.sql());
                sql.push_str(" ILIKE ");
                sql.push_str(&self.rexpr.sql());
            }
            A_Expr_Kind::AEXPR_SIMILAR => {
                sql.push_str(&self.lexpr.sql());
                sql.push_str(" SIMILAR TO ");

                if let Node::FuncCall(func) = self.rexpr.as_ref().unwrap().as_ref() {
                    sql.push_str(&func.args.sql(", "));
                } else {
                    sql.push_str(&self.rexpr.sql());
                }
            }
            A_Expr_Kind::AEXPR_BETWEEN => {
                sql.push_str(&self.lexpr.sql());
                sql.push_str(" BETWEEN ");

                if let Node::List(nodes) = self.rexpr.as_ref().unwrap().as_ref() {
                    sql.push_str(&nodes[0].sql());
                    sql.push_str(" AND ");
                    sql.push_str(&nodes[1].sql());
                }
            }
            A_Expr_Kind::AEXPR_NOT_BETWEEN => {
                sql.push_str(&self.lexpr.sql());
                sql.push_str(" NOT BETWEEN ");

                if let Node::List(nodes) = self.rexpr.as_ref().unwrap().as_ref() {
                    sql.push_str(&nodes[0].sql());
                    sql.push_str(" AND ");
                    sql.push_str(&nodes[1].sql());
                }
            }
            A_Expr_Kind::AEXPR_BETWEEN_SYM => {
                sql.push_str(" BETWEEN SYMMETRIC ");
                sql.push_str(&self.lexpr.sql());
                sql.push_str(" AND ");
                sql.push_str(&self.rexpr.sql());
            }
            A_Expr_Kind::AEXPR_NOT_BETWEEN_SYM => {
                sql.push_str(" NOT BETWEEN SYMMETRIC ");
                sql.push_str(&self.lexpr.sql());
                sql.push_str(" AND ");
                sql.push_str(&self.rexpr.sql());
            }
            A_Expr_Kind::AEXPR_PAREN => {
                sql.push_str(&self.lexpr.sql_wrap("(", ")"));
            }
        }
        sql.push(')');

        sql
    }
}
```

## File: `src/nodes/a_indicies.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::Sql;
use postgres_parser::nodes::A_Indices;

impl Sql for A_Indices {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str(&self.lidx.sql());
        if self.is_slice {
            sql.push(':');
        }
        sql.push_str(&self.uidx.sql());

        sql
    }
}
```

## File: `src/nodes/a_indirection.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Len, Sql};

use postgres_parser::nodes::A_Indirection;
use postgres_parser::Node;

impl Sql for A_Indirection {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push('(');
        sql.push_str(&self.arg.sql());
        sql.push_str(&indirection_list(&self.indirection));
        sql.push(')');
        sql
    }
}

pub fn indirection_list(list: &Option<Vec<Node>>) -> String {
    let mut sql = String::new();

    if list.len() > 0 {
        for indirection in list.as_ref().unwrap() {
            match indirection {
                Node::A_Indices(a_indieces) => sql.push_str(&format!("[{}]", a_indieces.sql())),
                Node::Value(value) => sql.push_str(&format!(".{}", value.sql())),
                _ => unimplemented!("unsupported A_Indirection::indirection node type"),
            }
        }
    }
    sql
}
```

## File: `src/nodes/a_star.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::Sql;
use postgres_parser::nodes::A_Star;

impl Sql for A_Star {
    fn sql(&self) -> String {
        "*".into()
    }
}
```

## File: `src/nodes/access_priv.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Len, Sql, SqlIdent};
use postgres_parser::nodes::AccessPriv;

impl Sql for AccessPriv {
    fn sql(&self) -> String {
        let mut sql = String::new();

        if self.priv_name.is_none() {
            sql.push_str("ALL PRIVILEGES");
        } else {
            sql.push_str(&self.priv_name.sql_ident());
        }

        if self.cols.len() > 0 {
            sql.push('(');
            for (i, col) in self.cols.as_ref().unwrap().iter().enumerate() {
                if i > 0 {
                    sql.push_str(", ");
                }
                sql.push_str(&col.sql());
            }
            sql.push(')');
        }

        sql
    }
}
```

## File: `src/nodes/alias.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlIdent, SqlList};
use postgres_parser::nodes::Alias;

impl Sql for Alias {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str(" AS ");
        sql.push_str(&self.aliasname.sql_ident());
        sql.push_str(&self.colnames.sql_wrap(", ", "(", ")"));

        sql
    }
}
```

## File: `src/nodes/alter_collation_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlIdent};
use postgres_parser::nodes::AlterCollationStmt;

impl Sql for AlterCollationStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("ALTER COLLATION ");
        sql.push_str(&self.collname.sql_ident());
        sql.push_str(" REFRESH VERSION");

        sql
    }
}

impl Diff for AlterCollationStmt {}
```

## File: `src/nodes/alter_function_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlList};
use postgres_parser::nodes::AlterFunctionStmt;

impl Sql for AlterFunctionStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("ALTER ");
        sql.push_str(&self.objtype.sql());
        sql.push_str(&self.func.sql_prefix(" "));
        sql.push_str(&self.actions.sql(", "));

        sql
    }
}

impl Diff for AlterFunctionStmt {
    fn drop_stmt(&self) -> Option<String> {
        None
    }
}
```

## File: `src/nodes/alter_object_schema_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlIdent, SqlMaybeList};
use postgres_parser::nodes::AlterObjectSchemaStmt;

impl Sql for AlterObjectSchemaStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("ALTER ");
        sql.push_str(&self.objectType.sql());
        sql.push(' ');
        sql.push_str(&self.object.sql_maybe_list("."));
        sql.push_str(" SET SCHEMA ");
        sql.push_str(&self.newschema.sql_ident());

        sql
    }
}

impl Diff for AlterObjectSchemaStmt {}
```

## File: `src/nodes/alter_owner_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlMaybeList};
use postgres_parser::nodes::AlterOwnerStmt;

impl Sql for AlterOwnerStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("ALTER ");
        sql.push_str(&self.objectType.sql());
        sql.push(' ');
        sql.push_str(&self.object.sql_maybe_list("."));
        sql.push_str(" OWNER TO ");
        sql.push_str(&self.newowner.sql());

        sql
    }
}

impl Diff for AlterOwnerStmt {}
```

## File: `src/nodes/alter_table_cmd.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlMaybeList};
use postgres_parser::nodes::AlterTableCmd;
use postgres_parser::sys::AlterTableType;

impl Sql for AlterTableCmd {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push(' ');
        match self.subtype {
            AlterTableType::AT_SetRelOptions => {
                sql.push_str("SET (");
                sql.push_str(&self.def.sql_maybe_list(", "));
                sql.push(')');
            }

            _ => unimplemented!("AlterTableCmd::behavior = {:?}", self.behavior),
        }

        sql
    }
}
```

## File: `src/nodes/alter_table_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlList};
use postgres_parser::nodes::AlterTableStmt;

impl Sql for AlterTableStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("ALTER ");
        sql.push_str(&self.relkind.sql());
        sql.push(' ');
        if self.missing_ok {
            sql.push_str("IF EXISTS ");
        }
        if !self.relation.as_ref().unwrap().inh {
            sql.push_str("ONLY ");
        }
        sql.push_str(&self.relation.sql());
        sql.push_str(&self.cmds.sql(", "));

        sql
    }
}

impl Diff for AlterTableStmt {}
```

## File: `src/nodes/alter_type_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlList};
use postgres_parser::nodes::AlterTypeStmt;

impl Sql for AlterTypeStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        if let Some(options) = &self.options {
            sql.push_str("ALTER TYPE ");
            sql.push_str(&self.typeName.sql("."));
            sql.push_str(" ");
            sql.push_str("SET (");
            sql.push_str(&options.sql(","));
            sql.push_str(")");
        }

        sql
    }
}

impl Diff for AlterTypeStmt {
    fn drop_stmt(&self) -> Option<String> {
        None
    }
}
```

## File: `src/nodes/bool_expr.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Len, Sql, SqlList};
use postgres_parser::nodes::BoolExpr;
use postgres_parser::sys::BoolExprType;

impl Sql for BoolExpr {
    fn sql(&self) -> String {
        let mut sql = String::new();

        if self.args.len() > 1 {
            sql.push('(');
        }
        sql.push_str(&match self.boolop {
            BoolExprType::AND_EXPR => self.args.sql(" AND "),
            BoolExprType::OR_EXPR => self.args.sql(" OR "),
            BoolExprType::NOT_EXPR => self.args.sql_wrap_each(Some("NOT "), None),
        });
        if self.args.len() > 1 {
            sql.push(')');
        }

        sql
    }
}
```

## File: `src/nodes/boolean_test.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::Sql;
use postgres_parser::nodes::BooleanTest;
use postgres_parser::sys::BoolTestType;

impl Sql for BooleanTest {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str(&self.arg.sql());
        match self.booltesttype {
            BoolTestType::IS_TRUE => sql.push_str(" IS TRUE"),
            BoolTestType::IS_NOT_TRUE => sql.push_str(" IS NOT TRUE"),
            BoolTestType::IS_FALSE => sql.push_str(" IS FALSE"),
            BoolTestType::IS_NOT_FALSE => sql.push_str(" IS NOT FALSE"),
            BoolTestType::IS_UNKNOWN => sql.push_str(" IS UNKNOWN"),
            BoolTestType::IS_NOT_UNKNOWN => sql.push_str(" IS NOT UNKNOWN"),
        }

        sql
    }
}
```

## File: `src/nodes/case_expr.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlList};
use postgres_parser::nodes::CaseExpr;

impl Sql for CaseExpr {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("CASE");

        if self.arg.is_some() {
            sql.push(' ');
            sql.push_str(&self.arg.sql());
        }

        sql.push(' ');
        sql.push_str(&self.args.sql(" "));

        sql.push_str(&self.defresult.sql_prefix(" ELSE "));
        sql.push_str(" END");

        sql
    }
}
```

## File: `src/nodes/case_when.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::Sql;
use postgres_parser::nodes::CaseWhen;

impl Sql for CaseWhen {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str(&self.expr.sql_prefix("WHEN "));
        sql.push_str(&self.result.sql_prefix(" THEN "));

        sql
    }
}
```

## File: `src/nodes/cluster_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlIdent};
use postgres_parser::nodes::ClusterStmt;
use postgres_parser::sys::ClusterOption;

impl Sql for ClusterStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("CLUSTER ");
        if self.options == ClusterOption::CLUOPT_VERBOSE as i32 {
            sql.push_str("VERBOSE ");
        }
        sql.push_str(&self.relation.sql());
        sql.push_str(&self.indexname.sql_ident_prefix(" USING "));

        sql
    }
}

impl Diff for ClusterStmt {}
```

## File: `src/nodes/cmd_type.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::Sql;
use postgres_parser::sys::CmdType;

impl Sql for CmdType {
    fn sql(&self) -> String {
        match self {
            CmdType::CMD_UNKNOWN => "UNKNOWN",
            CmdType::CMD_SELECT => "SELECT",
            CmdType::CMD_UPDATE => "UPDATE",
            CmdType::CMD_INSERT => "INSERT",
            CmdType::CMD_DELETE => "DELETE",
            CmdType::CMD_UTILITY => "UTILITY",
            CmdType::CMD_NOTHING => "NOTHING",
        }
        .into()
    }
}
```

## File: `src/nodes/coalesce_expr.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlList};
use postgres_parser::nodes::CoalesceExpr;

impl Sql for CoalesceExpr {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("COALESCE (");
        sql.push_str(&self.args.sql(", "));
        sql.push(')');

        sql
    }
}
```

## File: `src/nodes/coercion_context.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::Sql;
use postgres_parser::sys::CoercionContext;

impl Sql for CoercionContext {
    fn sql(&self) -> String {
        match self {
            CoercionContext::COERCION_IMPLICIT => " AS IMPLICIT",
            CoercionContext::COERCION_ASSIGNMENT => " AS ASSIGNMENT",
            CoercionContext::COERCION_EXPLICIT => "",
        }
        .into()
    }
}
```

## File: `src/nodes/collate_clause.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::make_name;
use crate::schema_set::Sql;
use postgres_parser::nodes::CollateClause;

impl Sql for CollateClause {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str(&self.arg.sql());
        sql.push_str(" COLLATE ");
        sql.push_str(&make_name(&self.collname).expect("unable to make CollateClause::collname"));

        sql
    }
}
```

## File: `src/nodes/column_def.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlIdent};
use crate::EMPTY_NODE_VEC;
use postgres_parser::nodes::ColumnDef;

impl Sql for ColumnDef {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str(&self.colname.sql_ident());
        sql.push(' ');
        sql.push_str(&self.typeName.sql());

        sql.push_str(&self.collClause.sql());
        for constraint in self.constraints.as_ref().unwrap_or(&EMPTY_NODE_VEC) {
            sql.push(' ');
            sql.push_str(&constraint.sql());
        }

        sql
    }
}
```

## File: `src/nodes/column_ref.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::SqlIdent;
use postgres_parser::nodes::ColumnRef;

impl SqlIdent for ColumnRef {
    fn sql_ident(&self) -> String {
        self.fields.sql_ident()
    }

    fn sql_ident_prefix(&self, pre: &str) -> String {
        format!("{}{}", pre, self.sql_ident())
    }

    fn sql_ident_suffix(&self, suf: &str) -> String {
        format!("{}{}", self.sql_ident(), suf)
    }
}
```

## File: `src/nodes/comment_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlMaybeList};
use postgres_parser::nodes::CommentStmt;

impl Sql for CommentStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("COMMENT ON ");
        sql.push_str(&self.objtype.sql());
        sql.push(' ');
        sql.push_str(&self.object.sql_maybe_list("."));
        sql.push_str(" IS ");

        if self.comment.is_some() {
            sql.push_str("'");
            sql.push_str(&self.comment.as_ref().unwrap().replace("'", "''"));
            sql.push_str("'");
        } else {
            sql.push_str("NULL");
        }

        sql
    }
}

impl Diff for CommentStmt {}
```

## File: `src/nodes/common_table_expr.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlIdent, SqlList};
use postgres_parser::nodes::CommonTableExpr;

impl Sql for CommonTableExpr {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str(&self.ctename.sql_ident());
        sql.push_str(&self.aliascolnames.sql_wrap(", ", "(", ")"));
        sql.push_str(" AS (");
        sql.push_str(&self.ctequery.sql());
        sql.push_str(") ");

        sql
    }
}
```

## File: `src/nodes/composite_type_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlList};
use postgres_parser::nodes::CompositeTypeStmt;

impl Sql for CompositeTypeStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("CREATE TYPE ");

        // we don't want .inh=false b/c that'll cause the RangeVar to output an "ONLY" and that's
        // not a thing here
        let mut typevar = self.typevar.clone();
        typevar.as_mut().unwrap().inh = true;
        sql.push_str(&typevar.sql());

        sql.push_str(" AS ");
        sql.push_str(&self.coldeflist.sql_wrap(", ", "(", ")"));
        sql
    }
}

impl Diff for CompositeTypeStmt {}
```

## File: `src/nodes/constraint.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Len, Sql, SqlIdent, SqlList};
use crate::{make_individual_names, EMPTY_NODE_VEC};
use postgres_parser::nodes::Constraint;
use postgres_parser::sys::ConstrType;
use postgres_parser::Node;

impl Sql for Constraint {
    fn sql(&self) -> String {
        let mut sql = String::new();

        match self.contype {
            ConstrType::CONSTR_NOTNULL => sql.push_str("NOT NULL"),
            ConstrType::CONSTR_NULL => sql.push_str("NULL"),
            ConstrType::CONSTR_PRIMARY => {
                sql.push_str("PRIMARY KEY");

                if !self.keys.is_empty() {
                    sql.push('(');
                    sql.push_str(&self.keys.sql(", "));
                    sql.push(')');
                }

                if self.deferrable {
                    sql.push_str(" DEFERRABLE ");
                }
            }
            ConstrType::CONSTR_DEFAULT => {
                sql.push_str("DEFAULT ");
                sql.push_str(
                    &self
                        .raw_expr
                        .as_ref()
                        .expect("no raw_expr for Constraint")
                        .sql(),
                );
            }

            ConstrType::CONSTR_IDENTITY => {
                if self.generated_when == 'a' {
                    sql.push_str("GENERATED ALWAYS ");
                } else {
                    sql.push_str("AS DEFAULT ");
                }

                sql.push_str("AS IDENTITY ");
                sql.push('(');
                sql.push_str(&self.options.sql_ident());
                sql.push(')');
            }
            ConstrType::CONSTR_GENERATED => {
                sql.push_str("GENERATED ALWAYS AS ");
                sql.push_str(&self.raw_expr.sql_wrap("(", ")"));
                sql.push_str(" STORED");
            }
            ConstrType::CONSTR_UNIQUE => {
                sql.push_str("UNIQUE");
                sql.push_str(&self.keys.sql_wrap(", ", "(", ")"));
                sql.push_str(
                    &self
                        .including
                        .sql_prefix_and_wrap(" INCLUDE ", "(", ")", ", "),
                );
                if self.options.is_some() {
                    sql.push_str(" WITH (");
                    for opt in self.options.as_ref().unwrap_or(&EMPTY_NODE_VEC) {
                        if let Node::DefElem(def_elem) = opt {
                            sql.push_str(&def_elem.defname.sql_ident());
                            sql.push_str(&def_elem.arg.sql_prefix("="));
                        } else {
                            panic!("unexpected 'options' element in Constraint::CONSTR_UNIQUE")
                        }
                    }
                    sql.push(')');
                }
                sql.push_str(&self.indexspace.sql_ident_prefix(" USING INDEX TABLESPACE "))
            }
            ConstrType::CONSTR_CHECK => {
                sql.push_str(&self.raw_expr.sql_prefix_and_wrap("CHECK ", "(", ")"));
                if self.is_no_inherit {
                    sql.push_str(" NO INHERIT");
                }
            }
            ConstrType::CONSTR_FOREIGN => {
                sql.push_str(&self.conname.sql_ident_prefix("CONSTRAINT "));

                if self.fk_attrs.is_some() {
                    sql.push_str(" FOREIGN KEY ");
                    sql.push('(');
                    sql.push_str(
                        &make_individual_names(&self.fk_attrs)
                            .into_iter()
                            .collect::<Vec<_>>()
                            .join(", "),
                    );
                    sql.push(')');
                }

                sql.push_str(" REFERENCES ");
                sql.push_str(&self.pktable.sql());
                if self.pk_attrs.is_some() {
                    sql.push('(');
                    sql.push_str(
                        &make_individual_names(&self.pk_attrs)
                            .into_iter()
                            .collect::<Vec<_>>()
                            .join(", "),
                    );
                    sql.push(')');
                }

                match self.fk_matchtype {
                    'f' => sql.push_str(" MATCH FULL"),
                    'p' => sql.push_str(" MATCH PARTIAL"),
                    's' => sql.push_str(" MATCH SIMPLE"),
                    _ => {}
                }

                /*
                   #define FKCONSTR_ACTION_NOACTION	'a'
                   #define FKCONSTR_ACTION_RESTRICT	'r'
                   #define FKCONSTR_ACTION_CASCADE		'c'
                   #define FKCONSTR_ACTION_SETNULL		'n'
                   #define FKCONSTR_ACTION_SETDEFAULT	'd'
                */
                match self.fk_del_action {
                    'a' => sql.push_str(" ON DELETE NO ACTION"),
                    'r' => sql.push_str(" ON DELETE RESTRICT"),
                    'c' => sql.push_str(" ON DELETE CASCADE"),
                    'n' => sql.push_str(" ON DELETE SET NULL"),
                    'd' => sql.push_str(" ON DELETE SET DEFAULT"),
                    _ => {}
                }
                match self.fk_upd_action {
                    'a' => sql.push_str(" ON UPDATE NO ACTION"),
                    'r' => sql.push_str(" ON UPDATE RESTRICT"),
                    'c' => sql.push_str(" ON UPDATE CASCADE"),
                    'n' => sql.push_str(" ON UPDATE SET NULL"),
                    'd' => sql.push_str(" ON UPDATE SET DEFAULT"),
                    _ => {}
                }
            }
            _ => unimplemented!("{:?}", self.contype),
        }

        sql
    }
}
```

## File: `src/nodes/copy_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Len, Sql, SqlList};
use postgres_parser::nodes::CopyStmt;

impl Sql for CopyStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("COPY ");

        if self.query.is_some() {
            sql.push_str(&self.query.sql_wrap("(", ")"))
        } else {
            sql.push_str(&self.relation.sql());
            if !self.attlist.is_empty() {
                sql.push_str(&self.attlist.sql_wrap(", ", "(", ")"))
            }
        }

        if self.is_from {
            sql.push_str(" FROM ");
            if self.filename.is_some() {
                if self.is_program {
                    sql.push_str("PROGRAM ");
                }
                sql.push_str(&format!("'{}'", self.filename.as_ref().unwrap()));
            } else {
                sql.push_str("STDIN");
            }
        } else {
            sql.push_str(" TO ");
            if self.filename.is_some() {
                if self.is_program {
                    sql.push_str("PROGRAM ");
                }
                sql.push_str(&format!("'{}'", self.filename.as_ref().unwrap()));
            } else {
                sql.push_str("STDOUT");
            }
        }

        if self.options.is_some() {
            sql.push_str(" WITH (");
            sql.push_str(&self.options.sql(", "));
            sql.push(')');
        }

        if self.whereClause.is_some() {
            sql.push_str(" WHERE ");
            sql.push_str(&self.whereClause.sql());
        }

        sql
    }
}

impl Diff for CopyStmt {}
```

## File: `src/nodes/create_am_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlIdent};
use postgres_parser::nodes::CreateAmStmt;

impl Sql for CreateAmStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("CREATE ACCESS METHOD ");
        sql.push_str(&self.amname.sql_ident());
        sql.push_str(" TYPE ");
        match self.amtype {
            't' => sql.push_str("TABLE"),
            'i' => sql.push_str("INDEX"),
            _ => panic!("unexpected CreateAmStmt::amtype"),
        }
        sql.push_str(" HANDLER ");
        sql.push_str(&self.handler_name.sql_ident());

        sql
    }
}

impl Diff for CreateAmStmt {
    fn object_name(&self) -> Option<String> {
        Some(self.amname.sql_ident())
    }

    fn object_type(&self) -> String {
        "ACCESS METHOD".into()
    }
}
```

## File: `src/nodes/create_cast_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql};
use postgres_parser::nodes::CreateCastStmt;

impl Sql for CreateCastStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("CREATE CAST");
        sql.push('(');
        sql.push_str(&self.sourcetype.sql());
        sql.push_str(" AS ");
        sql.push_str(&self.targettype.sql());
        sql.push(')');

        if self.func.is_some() {
            sql.push_str(&self.func.sql_prefix(" WITH FUNCTION "));
        } else {
            if self.inout {
                sql.push_str(" WITH INOUT ");
            } else {
                sql.push_str(" WITHOUT FUNCTION ");
            }
        }

        sql.push_str(&self.context.sql());

        sql
    }
}

impl Diff for CreateCastStmt {
    fn drop_stmt(&self) -> Option<String> {
        Some(format!(
            "DROP CAST IF EXISTS ({} AS {})",
            self.sourcetype.sql(),
            self.targettype.sql()
        ))
    }
}
```

## File: `src/nodes/create_conversion_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlIdent};
use postgres_parser::nodes::CreateConversionStmt;

impl Sql for CreateConversionStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("CREATE ");
        if self.def {
            sql.push_str("DEFAULT ");
        }
        sql.push_str("CONVERSION ");
        sql.push_str(&self.conversion_name.sql_ident());
        sql.push_str(" FOR '");
        sql.push_str(&self.for_encoding_name.as_ref().unwrap());
        sql.push_str("' TO '");
        sql.push_str(&self.to_encoding_name.as_ref().unwrap());
        sql.push_str("' FROM ");
        sql.push_str(&self.func_name.sql_ident());

        sql
    }
}

impl Diff for CreateConversionStmt {}
```

## File: `src/nodes/create_domain_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::make_name;
use crate::schema_set::{Diff, Sql, SqlIdent, SqlList};
use postgres_parser::nodes::CreateDomainStmt;

impl Sql for CreateDomainStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("CREATE DOMAIN ");
        sql.push_str(&self.domainname.sql_ident());
        sql.push_str(" AS ");
        sql.push_str(&self.typeName.sql());

        sql.push_str(&self.collClause.sql());
        sql.push_str(&self.constraints.sql_prefix(" ", " "));

        sql
    }
}

impl Diff for CreateDomainStmt {
    fn object_name(&self) -> Option<String> {
        Some(make_name(&self.domainname).expect("unable to make CreateDomainStmt::domainname"))
    }

    fn object_type(&self) -> String {
        "DOMAIN".into()
    }

}
```

## File: `src/nodes/create_enum_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlIdent, SqlList};
use postgres_parser::nodes::CreateEnumStmt;

impl Sql for CreateEnumStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("CREATE TYPE ");
        sql.push_str(&self.typeName.sql_ident());
        sql.push_str(" AS ENUM ");
        sql.push('(');
        sql.push_str(&self.vals.sql_wrap_each_and_separate(", ", "'", "'"));
        sql.push(')');

        sql
    }
}

impl Diff for CreateEnumStmt {
    fn drop_stmt(&self) -> Option<String> {
        Some(format!("DROP TYPE {}", self.sql()))
    }

    fn object_name(&self) -> Option<String> {
        Some(self.typeName.sql_ident())
    }

    fn object_type(&self) -> String {
        "ENUM".into()
    }
}
```

## File: `src/nodes/create_event_trig_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlIdent, SqlList};
use postgres_parser::nodes::CreateEventTrigStmt;

impl Sql for CreateEventTrigStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("CREATE EVENT TRIGGER ");
        sql.push_str(&self.trigname.sql_ident());
        sql.push_str(" ON ");
        sql.push_str(&self.eventname.sql_ident());

        if let Some(when) = &self.whenclause {
            sql.push_str(" WHEN ");
            sql.push_str(&when.sql(" AND "));
        }

        sql.push_str("EXECUTE FUNCTION ");
        sql.push_str(&self.funcname.sql_ident());
        sql.push_str("()");
        sql
    }
}

impl Diff for CreateEventTrigStmt {
    fn object_name(&self) -> Option<String> {
        Some(self.trigname.sql_ident())
    }

    fn object_type(&self) -> String {
        "EVENT TRIGGER".into()
    }
}
```

## File: `src/nodes/create_fdw_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlIdent, SqlList};
use postgres_parser::nodes::CreateFdwStmt;

impl Sql for CreateFdwStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("CREATE FOREIGN DATA WRAPPER ");
        sql.push_str(&self.fdwname.sql_ident());
        sql.push(' ');
        sql.push_str(&self.func_options.sql(" "));
        sql.push_str(&self.options.sql_prefix_and_wrap(" OPTIONS", "(", ")", ", "));

        sql
    }
}

impl Diff for CreateFdwStmt {}
```

## File: `src/nodes/create_foreign_server_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql};
use postgres_parser::nodes::CreateForeignServerStmt;

impl Sql for CreateForeignServerStmt {
    fn sql(&self) -> String {
        unimplemented!()
    }
}

impl Diff for CreateForeignServerStmt {}
```

## File: `src/nodes/create_foreign_table_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql};
use postgres_parser::nodes::CreateForeignTableStmt;

impl Sql for CreateForeignTableStmt {
    fn sql(&self) -> String {
        unimplemented!()
    }
}

impl Diff for CreateForeignTableStmt {}
```

## File: `src/nodes/create_function_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use std::cmp::Ordering;
use crate::schema_set::{Diff, Sql, SqlCollect, SqlIdent, SqlList};
use crate::{make_name, EMPTY_NODE_VEC};
use postgres_parser::nodes::CreateFunctionStmt;

use postgres_parser::sys::FunctionParameterMode::FUNC_PARAM_TABLE;
use postgres_parser::Node;

impl Sql for CreateFunctionStmt {
    fn sql(&self) -> String {
        let mut returns_table = false;
        let mut sql = String::new();

        if self.replace {
            sql.push_str("CREATE OR REPLACE ");
        } else {
            sql.push_str("CREATE ");
        }

        if self.is_procedure {
            sql.push_str("PROCEDURE ");
        } else {
            sql.push_str("FUNCTION ");
        }

        sql.push_str(&self.funcname.sql_ident());
        sql.push_str(
            &self
                .parameters
                .as_ref()
                .unwrap_or(&EMPTY_NODE_VEC)
                .iter()
                .filter(|p| match p {
                    Node::FunctionParameter(param) if param.mode != FUNC_PARAM_TABLE => true,
                    Node::FunctionParameter(param) if param.mode == FUNC_PARAM_TABLE => {
                        returns_table = true;
                        false
                    }
                    _ => false,
                })
                .map(|node| node.clone())
                .sql_wrap("(", ")"),
        );

        if returns_table {
            sql.push_str(" RETURNS TABLE");

            sql.push_str(
                &self
                    .parameters
                    .as_ref()
                    .unwrap_or(&EMPTY_NODE_VEC)
                    .iter()
                    .filter(|p|
                        matches!(p, Node::FunctionParameter(param) if param.mode == FUNC_PARAM_TABLE)
                    )
                    .map(|node| node.clone())
                    .sql_wrap("(", ")"),
            );
        } else {
            sql.push_str(&self.returnType.sql_prefix(" RETURNS "));
        }

        let mut orig_options = self.options.clone();
        if let Some(mut options) = orig_options {
            options.sort_by(|a, b| match a {
                Node::DefElem(a_defelem) => {
                    if let Node::DefElem(b_defelem) = b {
                        return a_defelem.sql().cmp(&b_defelem.sql());
                    }

                    Ordering::Equal
                },

                _ => Ordering::Equal
            });
            orig_options = Some(options);
        }

        sql.push_str(&orig_options.sql_prefix(" ", " "));

        sql
    }
}

impl Diff for CreateFunctionStmt {
    fn alter_stmt(&self, other: &Node) -> Option<String> {
        let mut alter = String::new();
        alter.push_str(&self.drop_stmt().unwrap());
        alter.push_str(";\n");
        alter.push_str(&other.sql());
        Some(alter)
    }

    fn drop_stmt(&self) -> Option<String> {
        let mut drop = String::new();

        drop.push_str("DROP ");
        if self.is_procedure {
            drop.push_str("PROCEDURE ");
        } else {
            drop.push_str("FUNCTION ");
        }
        drop.push_str("IF EXISTS ");
        drop.push_str(&make_name(&self.funcname).expect("no 'funcname' for CreateFunctionStmt"));
        drop.push('(');
        drop.push_str(
            &self
                .parameters
                .as_ref()
                .unwrap_or(&EMPTY_NODE_VEC)
                .iter()
                .filter(|p| {
                    matches!(p,
                    Node::FunctionParameter(param) if param.mode != FUNC_PARAM_TABLE)
                })
                .map(|node| match node {
                    Node::FunctionParameter(fp) => {
                        let mut fp = fp.clone();
                        fp.defexpr = None;
                        Node::FunctionParameter(fp)
                    }
                    _ => panic!("unexpected function parameter node type"),
                })
                .sql(),
        );
        drop.push(')');
        Some(drop)
    }

    fn object_name(&self) -> Option<String> {
        let mut as_ = String::new();
        let mut is_c = false;
        for opt in self.options.iter().flatten() {
            if let Node::DefElem(defelem) = opt {
                if defelem.defname.as_ref().unwrap().eq_ignore_ascii_case("as") {
                    as_ = defelem.sql();
                    break;
                } else if defelem.defname.as_ref().unwrap().eq_ignore_ascii_case("language") {
                    is_c = true;
                }
            }
        }

        let name = make_name(&self.funcname).expect("unable to make name for CreateFunctionStatement");
        if is_c {
            Some(name + &as_)
        } else {
            Some(name)
        }
    }

    fn object_type(&self) -> String {
        "FUNCTION".into()
    }
}
```

## File: `src/nodes/create_op_class_item.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlList};
use postgres_parser::nodes::CreateOpClassItem;

impl Sql for CreateOpClassItem {
    fn sql(&self) -> String {
        let mut sql = String::new();

        match self.itemtype {
            1 => {
                sql.push_str("OPERATOR ");
                sql.push_str(&self.number.to_string());
                sql.push(' ');
                sql.push_str(&self.name.sql().replace('"', ""));
                sql.push(' ');
                sql.push_str(&self.order_family.sql(" "))
            }
            2 => {
                sql.push_str("FUNCTION ");
                sql.push_str(&self.number.to_string());
                sql.push(' ');
                sql.push_str(&self.name.sql());
            }
            3 => {
                sql.push_str("STORAGE ");
                sql.push_str(&self.storedtype.sql());
            }
            _ => panic!("unknoown CreateOptClassItem::itemtype: {}", self.itemtype),
        }

        sql
    }
}
```

## File: `src/nodes/create_op_class_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlIdent, SqlList};
use postgres_parser::nodes::CreateOpClassStmt;

impl Sql for CreateOpClassStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("CREATE OPERATOR CLASS ");
        sql.push_str(&self.opclassname.sql_ident());
        sql.push(' ');
        if self.isDefault {
            sql.push_str("DEFAULT ");
        }
        sql.push_str("FOR TYPE ");
        sql.push_str(&self.datatype.sql());
        sql.push_str(" USING ");
        sql.push_str(&self.amname.sql_ident());
        sql.push_str(&self.opfamilyname.sql_ident_prefix(" FAMILY "));
        sql.push_str(" AS ");
        sql.push_str(&self.items.sql(", "));

        sql
    }
}

impl Diff for CreateOpClassStmt {
    fn object_name(&self) -> Option<String> {
        Some(self.opclassname.sql_ident())
    }

    fn object_type(&self) -> String {
        "OP CLASS".into()
    }
}
```

## File: `src/nodes/create_policy_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlIdent, SqlList};
use postgres_parser::nodes::CreatePolicyStmt;

impl Sql for CreatePolicyStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("CREATE POLICY ");
        sql.push_str(&self.policy_name.sql_ident());
        sql.push_str(" ON ");
        sql.push_str(&self.table.sql());
        if self.permissive {
            sql.push_str(" AS PERMISSIVE ");
        } else {
            sql.push_str(" AS RESTRICTIVE ");
        }

        if self.cmd_name.is_none() {
            sql.push_str("FOR ALL ");
        } else {
            sql.push_str("FOR ");
            sql.push_str(&self.cmd_name.as_ref().unwrap().to_uppercase());
        }

        sql.push_str(&self.roles.sql_prefix(" TO ", ", "));
        sql.push_str(&self.qual.sql_prefix_and_wrap(" USING ", "(", ")"));
        sql.push_str(
            &self
                .with_check
                .sql_prefix_and_wrap(" WITH CHECK ", "(", ")"),
        );

        sql
    }
}

impl Diff for CreatePolicyStmt {}
```

## File: `src/nodes/create_range_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlIdent, SqlList};
use postgres_parser::nodes::CreateRangeStmt;

impl Sql for CreateRangeStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("CREATE TYPE ");
        sql.push_str(&self.typeName.sql_ident());
        sql.push_str(" AS RANGE (");
        sql.push_str(&self.params.sql(", "));
        sql.push(')');

        sql
    }
}

impl Diff for CreateRangeStmt {}
```

## File: `src/nodes/create_role_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlIdent, SqlList};
use postgres_parser::nodes::CreateRoleStmt;
use postgres_parser::sys::RoleStmtType;

impl Sql for CreateRoleStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("CREATE ");
        match self.stmt_type {
            RoleStmtType::ROLESTMT_ROLE => sql.push_str("ROLE "),
            RoleStmtType::ROLESTMT_USER => sql.push_str("USER "),
            RoleStmtType::ROLESTMT_GROUP => sql.push_str("GROUP "),
        }
        sql.push_str(&self.role.sql_ident());
        sql.push_str(&self.options.sql_prefix(" WITH ", " "));

        sql
    }
}

impl Diff for CreateRoleStmt {}
```

## File: `src/nodes/create_schema_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlIdent};
use postgres_parser::nodes::CreateSchemaStmt;
use postgres_parser::Node;

impl Sql for CreateSchemaStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("CREATE SCHEMA ");
        if self.if_not_exists {
            sql.push_str("IF NOT EXISTS ");
        }

        if self.authrole.is_some() {
            sql.push_str("AUTHORIZATION ");
            sql.push_str(&self.authrole.sql());
        } else {
            sql.push_str(&self.schemaname.sql_ident())
        }

        sql
    }
}

impl Diff for CreateSchemaStmt {
    fn alter_stmt(&self, other: &Node) -> Option<String> {
        if let Node::CreateSchemaStmt(other) = other {
            if self.authrole != other.authrole {
                let mut sql = String::new();

                sql.push_str("ALTER SCHEMA ");
                sql.push_str(&self.schemaname.sql_ident());
                sql.push_str(" OWNER TO ");
                sql.push_str(&self.authrole.sql());

                return Some(sql);
            }
        }

        None
    }

    fn drop_stmt(&self) -> Option<String> {
        let mut sql = String::new();
        sql.push_str("DROP SCHEMA ");
        sql.push_str(&self.schemaname.clone().unwrap());
        Some(sql)
    }

    fn object_name(&self) -> Option<String> {
        Some(self.schemaname.sql_ident())
    }

    fn object_type(&self) -> String {
        "SCHEMA".into()
    }
}
```

## File: `src/nodes/create_seq_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlList};
use postgres_parser::nodes::CreateSeqStmt;

impl Sql for CreateSeqStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        let is_temp = self.sequence.as_ref().unwrap().relpersistence == 't';
        sql.push_str("CREATE ");
        if is_temp {
            sql.push_str("TEMPORARY ");
        }
        sql.push_str("SEQUENCE ");
        if self.if_not_exists {
            sql.push_str("IF NOT EXISTS ");
        }
        sql.push_str(&self.sequence.sql());
        sql.push_str(&self.options.sql(" "));
        sql
    }
}

impl Diff for CreateSeqStmt {}
```

## File: `src/nodes/create_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlIdent, SqlList};

use postgres_parser::nodes::CreateStmt;

impl Sql for CreateStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        let is_temp = self.relation.as_ref().unwrap().relpersistence == 't';

        sql.push_str("CREATE ");
        if is_temp {
            sql.push_str("TEMPORARY ");
        }
        sql.push_str("TABLE ");

        if self.if_not_exists {
            sql.push_str("IF NOT EXISTS ");
        }

        sql.push_str(&self.relation.sql());

        if self.partbound.is_some() {
            sql.push_str(&self.inhRelations.sql_prefix(" PARTITION OF ", ", "));
            sql.push_str(&self.partbound.sql_prefix(" "));
        } else {
            sql.push('(');
            sql.push_str(&self.tableElts.sql(", "));
            sql.push(')');
        }

        if self.partbound.is_none() {
            sql.push_str(
                &self
                    .inhRelations
                    .sql_prefix_and_wrap(" INHERITS ", "(", ")", ", "),
            );
        }
        sql.push_str(&self.partspec.sql_prefix(" PARTITION BY "));
        sql.push_str(&self.accessMethod.sql_ident_prefix(" USING "));
        sql.push_str(&self.options.sql_prefix_and_wrap(" WITH ", "(", ")", ", "));
        sql.push_str(&self.oncommit.sql_prefix(" "));

        sql
    }
}

impl Diff for CreateStmt {
    fn object_name(&self) -> Option<String> {
        Some(self.relation.sql())
    }

    fn object_type(&self) -> String {
        "RELATION".into()
    }
}
```

## File: `src/nodes/create_table_as_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql};
use postgres_parser::nodes::CreateTableAsStmt;

impl Sql for CreateTableAsStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("CREATE ");
        if self.into.is_some() {
            if self
                .into
                .as_ref()
                .unwrap()
                .rel
                .as_ref()
                .unwrap()
                .relpersistence
                == 't'
            {
                sql.push_str("TEMPORARY ");
            }
        }

        sql.push_str(&self.relkind.sql());
        sql.push(' ');

        if self.if_not_exists {
            sql.push_str("IF NOT EXISTS ");
        }
        sql.push_str(&self.into.sql());
        sql.push_str(" AS ");
        sql.push_str(&self.query.sql());

        if self.into.is_some() {
            if self.into.as_ref().unwrap().skipData {
                sql.push_str(" WITH NO DATA");
            } else {
                sql.push_str(" WITH DATA");
            }
        }

        sql
    }
}

impl Diff for CreateTableAsStmt {}
```

## File: `src/nodes/create_trig_stmt.rs`
```rust
#![allow(dead_code)]
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlIdent, SqlList};
use postgres_parser::nodes::CreateTrigStmt;

const TRIGGER_TYPE_AFTER: i16 = 0;
const TRIGGER_TYPE_ROW: i16 = 1 << 0;
const TRIGGER_TYPE_BEFORE: i16 = 1 << 1;
const TRIGGER_TYPE_INSERT: i16 = 1 << 2;
const TRIGGER_TYPE_DELETE: i16 = 1 << 3;
const TRIGGER_TYPE_UPDATE: i16 = 1 << 4;
const TRIGGER_TYPE_TRUNCATE: i16 = 1 << 5;
const TRIGGER_TYPE_INSTEAD: i16 = 1 << 6;

impl Sql for CreateTrigStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("CREATE ");
        if self.isconstraint {
            sql.push_str("CONSTRAINT ");
        }
        sql.push_str("TRIGGER ");
        sql.push_str(&self.trigname.sql_ident());

        if self.timing & TRIGGER_TYPE_BEFORE == TRIGGER_TYPE_BEFORE {
            sql.push_str(" BEFORE");
        } else if self.timing & TRIGGER_TYPE_INSTEAD == TRIGGER_TYPE_INSTEAD {
            sql.push_str(" INSTEAD OF");
        } else if self.timing & TRIGGER_TYPE_INSTEAD == TRIGGER_TYPE_AFTER {
            sql.push_str(" AFTER");
        }

        let mut have_type = false;
        if self.events & TRIGGER_TYPE_INSERT == TRIGGER_TYPE_INSERT {
            sql.push_str(" INSERT ");
            have_type = true;
        }

        if self.events & TRIGGER_TYPE_UPDATE == TRIGGER_TYPE_UPDATE {
            if have_type {
                sql.push_str("OR")
            }
            sql.push_str(" UPDATE ");
            have_type = true;
        }

        if self.events & TRIGGER_TYPE_DELETE == TRIGGER_TYPE_DELETE {
            if have_type {
                sql.push_str("OR")
            }
            sql.push_str(" DELETE ");
            have_type = true;
        }

        if self.events & TRIGGER_TYPE_TRUNCATE == TRIGGER_TYPE_TRUNCATE {
            if have_type {
                sql.push_str("OR")
            }
            sql.push_str(" TRUNCATE ");
        }

        sql.push_str("ON ");
        sql.push_str(&self.relation.sql());
        sql.push(' ');

        if self.isconstraint {
            if self.deferrable {
                sql.push_str("DEFERRABLE ");
            } else {
                sql.push_str("NOT DEFERRABLE ");
            }

            if self.initdeferred {
                sql.push_str("INITIALLY DEFERRED ");
            } else {
                sql.push_str("INITIALLY IMMEDIATE ");
            }
        }

        sql.push_str("FOR EACH ");
        if self.row {
            sql.push_str("ROW ");
        } else {
            sql.push_str("STATEMENT ");
        }

        sql.push_str("EXECUTE PROCEDURE ");
        sql.push_str(&self.funcname.sql_ident());
        if self.args.is_some() {
            sql.push_str(&self.args.sql_wrap(", ", "(", ")"));
        } else {
            sql.push_str("()");
        }

        sql
    }
}

impl Diff for CreateTrigStmt {}
```

## File: `src/nodes/current_of_expr.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlIdent};
use postgres_parser::nodes::CurrentOfExpr;

impl Sql for CurrentOfExpr {
    fn sql(&self) -> String {
        format!("CURRENT OF {}", self.cursor_name.sql_ident())
    }
}
```

## File: `src/nodes/declare_cursor_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlIdent};
use postgres_parser::nodes::DeclareCursorStmt;

impl Sql for DeclareCursorStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("DECLARE ");
        sql.push_str(&self.portalname.sql_ident());

        if self.options & 0x0001 != 0 {
            sql.push_str(" BINARY");
        }

        if self.options & 0x0008 != 0 {
            sql.push_str(" INSENSITIVE");
        }

        if self.options & 0x0002 != 0 {
            sql.push_str(" SCROLL");
        }

        if self.options & 0x0004 != 0 {
            sql.push_str(" NO SCROLL");
        }

        sql.push_str(" CURSOR");

        if self.options & 0x0010 != 0 {
            sql.push_str(" WITH HOLD");
        } else {
            sql.push_str(" WITHOUT HOLD");
        }

        sql.push_str(" FOR ");
        sql.push_str(&self.query.sql());

        sql
    }
}

impl Diff for DeclareCursorStmt {}
```

## File: `src/nodes/def_elem.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlMaybeList};
use crate::{get_bool_value, make_name};
use postgres_parser::nodes::DefElem;
use postgres_parser::Node;

impl Sql for DefElem {
    fn sql(&self) -> String {
        let mut sql = String::new();

        let defname = self.defname.as_ref().unwrap();

        match defname.as_str() {
            "cache" => sql.push_str(&format!("CACHE {}", self.arg.sql())),
            "cycle" => {
                if get_bool_value(&self.arg.as_ref().unwrap()) {
                    sql.push_str("CYCLE");
                } else {
                    sql.push_str("NO CYCLE");
                }
            }
            "language" => {
                sql.push_str(&format!("LANGUAGE {}", self.arg.sql()));
            }
            "volatility" => {
                sql.push_str(&self.arg.sql().to_uppercase());
            }
            "strict" => {
                if get_bool_value(&self.arg.as_ref().unwrap()) {
                    sql.push_str("STRICT");
                }
            }
            "set" => {
                sql.push_str(&self.arg.sql());
            }
            "parallel" => sql.push_str(&format!(
                "PARALLEL{}{}",
                separator(&self.arg.as_ref().unwrap()),
                self.arg.sql().to_uppercase()
            )),
            "cost" => sql.push_str(&format!("COST {}", self.arg.sql())),
            "rows" => sql.push_str(&format!("ROWS {}", self.arg.sql())),
            "start" => sql.push_str(&format!("START WITH {}", &self.arg.sql())),
            "procedure" => sql.push_str(&format!("PROCEDURE = {}", self.arg.sql())),
            "restrict" => sql.push_str(&format!("RESTRICT = {}", self.arg.sql())),
            "leftarg" => sql.push_str(&format!("LEFTARG = {}", self.arg.sql())),
            "rightarg" => sql.push_str(&format!("RIGHTARG = {}", self.arg.sql())),

            "null" => {
                if self.arg.is_some() {
                    let arg = self.arg.sql();
                    if arg.len() == 0 {
                        sql.push_str("NULL ''");
                    } else {
                        sql.push_str(&format!("NULL '{}'", arg));
                    }
                } else {
                    sql.push_str("NULL ''");
                }
            }
            "header" => sql.push_str(&format!("HEADER {}", scalar(self.arg.sql()))),
            "encoding" => sql.push_str(&format!("ENCODING {}", scalar(self.arg.sql()))),
            "format" => sql.push_str(&format!("FORMAT {}", scalar(self.arg.sql()))),
            "freeze" => sql.push_str(&format!("FREEZE {}", scalar(self.arg.sql()))),

            "force_quote" => {
                sql.push_str(&format!("FORCE_QUOTE ({})", self.arg.sql_maybe_list(", ")))
            }

            "force_null" => {
                sql.push_str(&format!("FORCE_NULL ({})", self.arg.sql_maybe_list(", ")))
            }

            "force_not_null" => sql.push_str(&format!(
                "FORCE_NOT_NULL ({})",
                self.arg.sql_maybe_list(", ")
            )),

            "costs" => sql.push_str(&format!("COSTS {}", scalar(self.arg.sql()))),

            "stype" => sql.push_str(&format!("STYPE = {}", self.arg.sql())),
            "sfunc" => sql.push_str(&format!("SFUNC = {}", self.arg.sql())),
            "finalfunc" => sql.push_str(&format!("FINALFUNC = {}", self.arg.sql())),
            "initcond" => sql.push_str(&format!("INITCOND = '{}'", self.arg.sql())),
            "transaction_isolation" => {
                sql.push_str("ISOLATION LEVEL ");
                match self.arg.as_ref().unwrap().as_ref() {
                    Node::A_Const(a_const) => sql.push_str(&a_const.val.sql().to_uppercase()),
                    _ => panic!("unsupported arg node type for transaction_isolation"),
                }
            }
            "transaction_deferrable" => match self.arg.as_ref().unwrap().as_ref() {
                Node::A_Const(a_const) => {
                    if a_const.val.int.unwrap_or(1) == 1 {
                        sql.push_str(" DEFERRABLE");
                    } else {
                        sql.push_str(" NOT DEFERRABLE");
                    }
                }
                _ => panic!("unsupported arg node type for transaction_deferrable"),
            },
            "autovacuum_enabled" => {
                sql.push_str(&format!("autovacuum_enabled = {}", self.arg.sql()))
            }
            "deduplicate_items" => sql.push_str(&format!("deduplicate_items = {}", self.arg.sql())),

            "as" if self.arg.is_some() => {
                let unboxed = self.arg.as_ref().unwrap();
                if let Node::Value(value) = unboxed.as_ref() {
                    sql.push_str(&quote(value.sql()));
                } else if let Node::List(list) = unboxed.as_ref() {
                    sql.push_str("AS ");
                    for (i, node) in list.iter().enumerate() {
                        if i > 0 {
                            sql.push_str(", ");
                        }
                        sql.push_str(&quote(node.sql()));
                    }
                } else {
                    sql.push_str(&self.arg.sql());
                }
            }

            "from" => {
                if let Node::List(list) = self.arg.as_ref().unwrap().as_ref() {
                    sql.push_str(&format!("FROM {}", make_name(&Some(list.clone())).unwrap()));
                } else {
                    panic!("unexpected node type for 'from' DefElem")
                }
            }

            "delimiter" => sql.push_str(&format!(
                "delimiter '{}'",
                self.arg.sql().replace("'", "''")
            )),

            "provider" => sql.push_str(&format!("provider = {}", self.arg.sql())),
            "collation" => sql.push_str(&format!("collation = {}", self.arg.sql())),
            "subtype" => sql.push_str(&format!("subtype = {}", self.arg.sql())),
            "locale" => sql.push_str(&format!("locale = '{}'", self.arg.sql())),
            "lc_ctype" => sql.push_str(&format!("lc_ctype = {}", self.arg.sql())),
            "lc_collate" => sql.push_str(&format!("lc_collate = {}", self.arg.sql())),

            "createdb" => {
                if let Node::Value(value) = self.arg.as_ref().unwrap().as_ref() {
                    if value.int.unwrap_or_default() == 0 {
                        sql.push_str("NOCREATEDB");
                    } else {
                        sql.push_str("CREATEDB");
                    }
                }
            }
            "createrole" => {
                if let Node::Value(value) = self.arg.as_ref().unwrap().as_ref() {
                    if value.int.unwrap_or_default() == 0 {
                        sql.push_str("NOCREATEROLE");
                    } else {
                        sql.push_str("CREATEROLE");
                    }
                }
            }

            key => {
                if self.arg.is_some() {
                    let arg_sql = self.arg.sql();

                    let uppercase_cnt = key.chars().filter(|c| c.is_uppercase()).count();

                    let key = if uppercase_cnt > 0 {
                        format!("\"{}\"", key)
                    } else {
                        key.into()
                    };

                    if arg_sql.starts_with('"') && arg_sql.ends_with('"') {
                        sql.push_str(&format!("{} = {}", key, arg_sql))
                    } else {
                        sql.push_str(&format!("{} = {}", key, scalar(arg_sql)))
                    }
                } else {
                    sql.push_str(key)
                }
            }
        }

        sql
    }
}

fn quote(input: String) -> String {
    if input.contains('\'') {
        if input.contains("$$") {
            if input.contains("$_pgsdq$") {
                // just something random
                let quote: [char; 15] = rand::random();
                let quote: String = quote.iter().collect();
                format!("${}${}${}$", quote, input, quote)
            } else {
                format!("$_pgsdq${}$_pgsdq$", input)
            }
        } else {
            format!("$${}$$", input)
        }
    } else {
        format!("'{}'", input)
    }
}

fn scalar(input: String) -> String {
    for c in input.chars() {
        if !['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-'].contains(&c) {
            return format!("'{}'", input.replace('\'', "''"));
        }
    }

    input
}

fn separator(input: &Node) -> &'static str {
    if let Node::Value(_) = input {
        " "
    } else if let Node::TypeName(_) = input {
        " = "
    } else {
        panic!("cannot determine separator")
    }
}
```

## File: `src/nodes/define_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Len, Sql, SqlIdent, SqlList};
use postgres_parser::nodes::DefineStmt;
use postgres_parser::sys::ObjectType;
use postgres_parser::Node;
use std::borrow::Cow;
use std::collections::HashMap;

impl Sql for DefineStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("CREATE ");
        if self.replace {
            sql.push_str("OR REPLACE ");
        }
        sql.push_str(&self.kind.sql());
        sql.push(' ');
        sql.push_str(&self.defnames.sql("."));

        match self.kind {
            ObjectType::OBJECT_COLLATION => {
                if self.definition.len() == 1 {
                    if let Node::DefElem(defelem) =
                        self.definition.as_ref().unwrap().get(0).unwrap()
                    {
                        if defelem.defname == Some("from".into()) {
                            sql.push(' ');
                            sql.push_str(&defelem.sql())
                        } else {
                            sql.push('(');
                            sql.push_str(&self.definition.sql_prefix(" ", ", "));
                            sql.push(')');
                        }
                    } else {
                        panic!(
                            "unexpected DefineStmt::definition node: {:#?}",
                            self.definition
                        );
                    }
                } else {
                    sql.push_str(&self.definition.sql_prefix_and_wrap(" ", "(", ")", ", "));
                }
            }

            ObjectType::OBJECT_OPERATOR | ObjectType::OBJECT_AGGREGATE => {
                if self.args.is_some() {
                    let args = self.args.as_ref().unwrap().get(0).unwrap();
                    if let Node::List(args) = args {
                        let marker = self.args.as_ref().unwrap().last().unwrap();

                        match marker {
                            Node::Value(value) => {
                                let ndirectargs = value.int.unwrap();
                                sql.push('(');

                                let mut iter = args.iter();
                                let mut i = 0;
                                while let Some(arg) = iter.next() {
                                    if i > 0 {
                                        sql.push_str(", ");
                                    }

                                    i += 1;
                                    if ndirectargs > -1 && i >= ndirectargs.max(0) as usize {
                                        let orderby = iter.next();

                                        if orderby.is_some() {
                                            sql.push_str(&arg.sql());
                                            sql.push_str(" ORDER BY ");
                                            sql.push_str(&orderby.unwrap().sql());
                                        } else {
                                            sql.push_str(&arg.sql());
                                            sql.push_str(" ORDER BY ");
                                            sql.push_str(&arg.sql());
                                        }
                                    } else {
                                        sql.push_str(&arg.sql());
                                    }
                                }

                                sql.push(')');
                            }

                            _ => sql.push_str(&self.args.sql_wrap(", ", "(", ")")),
                        }
                    } else {
                        sql.push('(');
                        for arg in self.args.as_ref().unwrap() {
                            let arg = arg.sql();
                            if arg == "-1" {
                                sql.push('*');
                            } else {
                                sql.push_str(&arg);
                            }
                        }
                        sql.push(')');
                    }
                }

                sql.push('(');
                for (i, node) in self.definition.as_ref().unwrap().iter().enumerate() {
                    if let Node::DefElem(defelem) = node {
                        if i > 0 {
                            sql.push_str(", ");
                        }
                        if self.oldstyle {
                            sql.push('"');
                            sql.push_str(defelem.defname.as_ref().unwrap());
                            sql.push('"');
                        } else {
                            sql.push_str(defelem.defname.as_ref().unwrap());
                        }
                        if defelem.arg.is_some() {
                            sql.push('=');

                            let defname = &defelem.defname.as_ref().unwrap().to_lowercase();
                            if "initcond" == defname || "initcond1" == defname {
                                sql.push('\'');
                                sql.push_str(&defelem.arg.sql().replace("'", "''"));
                                sql.push('\'');
                            } else if Some("basetype".into()) == defelem.defname {
                                let arg = defelem.arg.sql();

                                if arg == "ANY" {
                                    sql.push('\'');
                                    sql.push_str(&defelem.arg.sql().replace("'", "''"));
                                    sql.push('\'');
                                } else {
                                    sql.push_str(&defelem.arg.sql());
                                }
                            } else {
                                sql.push_str(&defelem.arg.sql());
                            }
                        }
                    } else {
                        panic!("unexpected definition node for DefineStatement::ObjectType::OBJECT_OPERATOR");
                    }
                }
                sql.push(')');
            }
            _ => {
                if self.args.is_some() {
                    if self.kind != ObjectType::OBJECT_AGGREGATE {
                        sql.push_str(" AS ");
                    }

                    sql.push('(');
                    sql.push_str(&self.args.sql(", "));
                    sql.push(')');
                }
            }
        }

        sql
    }
}

impl Diff for DefineStmt {
    fn alter_stmt(&self, other: &Node) -> Option<String> {
        if matches!(self.kind, ObjectType::OBJECT_OPERATOR) {
            let my_defelems = self
                .definition
                .as_ref()
                .unwrap()
                .into_iter()
                .filter_map(|node| {
                    if let Node::DefElem(defelem) = node {
                        let name = defelem.defname.as_ref().unwrap();
                        Some((name.as_str(), defelem))
                    } else {
                        None
                    }
                })
                .collect::<HashMap<_, _>>();
            if let Node::DefineStmt(other) = other {
                let other_defelms = other
                    .definition
                    .as_ref()
                    .unwrap()
                    .into_iter()
                    .filter_map(|node| {
                        if let Node::DefElem(defelem) = node {
                            let name = defelem.defname.as_ref().unwrap();
                            Some((name.as_str(), defelem))
                        } else {
                            None
                        }
                    })
                    .collect::<HashMap<_, _>>();

                let my_lefttype = my_defelems
                    .get("leftarg")
                    .expect("OPERATOR should have a LEFTARG");
                let my_righttype = my_defelems
                    .get("rightarg")
                    .expect("OPERATOR should have a RIGHTARG");

                let args = format!("({}, {})", my_lefttype.sql(), my_righttype.sql());

                let mut sql = String::new();

                match (my_defelems.get("restrict"), other_defelms.get("restrict")) {
                    (Some(mine), Some(theirs)) if mine != theirs => {
                        sql.push_str(&format!(
                            "ALTER OPERATOR {}{args} SET (RESTRICT = {});\n",
                            self.defnames.sql_ident(),
                            theirs.sql()
                        ));
                    }
                    (Some(_), None) => {
                        sql.push_str(&format!(
                            "ALTER OPERATOR {}{args} SET (RESTRICT = NONE);\n",
                            self.defnames.sql_ident()
                        ));
                    }
                    _ => {}
                }

                match (my_defelems.get("join"), other_defelms.get("join")) {
                    (Some(mine), Some(theirs)) if mine != theirs => {
                        sql.push_str(&format!(
                            "ALTER OPERATOR {}{args} SET (JOIN = {});\n",
                            self.defnames.sql_ident(),
                            theirs.sql()
                        ));
                    }
                    (Some(_), None) => {
                        sql.push_str(&format!(
                            "ALTER OPERATOR {}{args} SET (JOIN = NONE);\n",
                            self.defnames.sql_ident()
                        ));
                    }
                    _ => {}
                }

                let sql = sql.trim();
                return if sql.is_empty() {
                    None
                } else {
                    Some(sql.trim_end_matches(';').to_string())
                };
            }
        }
        // For non-OPERATOR types (e.g., AGGREGATE, COLLATION, etc.) or when other is not a DefineStmt,
        // we don't know how to generate ALTER statements, so return None (same as trait default).
        // Note: We can't call Diff::alter_stmt(self, other) here because it would resolve to
        // DefineStmt::alter_stmt again, causing infinite recursion.
        None
    }

    fn drop_stmt(&self) -> Option<String> {
        match self.kind {
            ObjectType::OBJECT_OPERATOR => {
                let Some(Node::DefElem(leftarg)) = self.definition.as_ref().unwrap().get(1) else {
                    panic!("bad operator definition")
                };
                let Some(Node::DefElem(rightarg)) = self.definition.as_ref().unwrap().get(2) else {
                    panic!("bad operator definition")
                };

                let sql = format!(
                    "DROP OPERATOR IF EXISTS {}({}, {})",
                    self.defnames.sql_ident(),
                    leftarg.arg.as_ref().unwrap().sql(),
                    rightarg.arg.as_ref().unwrap().sql()
                );

                Some(sql)
            }

            _ => Some(format!(
                "DROP {} IF EXISTS {}",
                self.kind.sql(),
                self.defnames.sql_ident()
            )),
        }
    }

    fn object_name(&self) -> Option<String> {
        Some(self.defnames.sql_ident())
    }

    fn object_type(&self) -> String {
        self.kind.sql()
    }

    fn identifier<'a>(&self, tree_string: &'a str) -> Cow<'a, str> {
        match self.kind {
            ObjectType::OBJECT_TYPE => {
                let mut sql = self.sql();
                if self.definition.is_none() || self.definition.as_ref().unwrap().is_empty() {
                    sql += " (shell type)";
                }
                Cow::Owned(sql)
            }
            ObjectType::OBJECT_OPERATOR => Cow::Owned(self.sql()),
            _ => match self.object_name() {
                Some(name) => Cow::Owned(name + &self.object_type()),
                None => Cow::Borrowed(tree_string),
            },
        }
    }
}
```

## File: `src/nodes/delete_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::nodes::res_target::res_target_returning;
use crate::schema_set::{Diff, Sql, SqlList};
use postgres_parser::nodes::DeleteStmt;

impl Sql for DeleteStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str(&self.withClause.sql());
        sql.push_str("DELETE FROM ");
        sql.push_str(&self.relation.sql());
        sql.push_str(&self.usingClause.sql_prefix(" USING ", ", "));
        sql.push_str(&self.whereClause.sql_prefix(" WHERE "));
        sql.push_str(&res_target_returning(&self.returningList));

        sql
    }
}

impl Diff for DeleteStmt {}
```

## File: `src/nodes/discard_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql};
use postgres_parser::nodes::DiscardStmt;
use postgres_parser::sys::DiscardMode;

impl Sql for DiscardMode {
    fn sql(&self) -> String {
        match self {
            DiscardMode::DISCARD_ALL => "ALL",
            DiscardMode::DISCARD_PLANS => "PLANS",
            DiscardMode::DISCARD_SEQUENCES => "SEQUENCES",
            DiscardMode::DISCARD_TEMP => "TEMP",
        }
        .into()
    }
}

impl Sql for DiscardStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("DISCARD ");
        sql.push_str(&self.target.sql());

        sql
    }
}

impl Diff for DiscardStmt {}
```

## File: `src/nodes/do_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlList};
use postgres_parser::nodes::DoStmt;

impl Sql for DoStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("DO ");
        sql.push_str(&self.args.sql(" "));

        sql
    }
}

impl Diff for DoStmt {
    fn drop_stmt(&self) -> Option<String> {
        None
    }
}
```

## File: `src/nodes/drop_behavior.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::Sql;
use postgres_parser::sys::DropBehavior;

impl Sql for DropBehavior {
    fn sql(&self) -> String {
        match self {
            DropBehavior::DROP_RESTRICT => "RESTRICT",
            DropBehavior::DROP_CASCADE => "CASCADE",
        }
        .into()
    }
}
```

## File: `src/nodes/drop_role_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlList};
use postgres_parser::nodes::DropRoleStmt;

impl Sql for DropRoleStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("DROP ROLE ");
        if self.missing_ok {
            sql.push_str("IF EXISTS ");
        }
        sql.push_str(&self.roles.sql(", "));

        sql
    }
}

impl Diff for DropRoleStmt {}
```

## File: `src/nodes/drop_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlIdent};
use postgres_parser::nodes::DropStmt;
use postgres_parser::sys::ObjectType;
use postgres_parser::Node;

impl Sql for DropStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("DROP ");
        sql.push_str(&self.removeType.sql());
        sql.push(' ');
        if self.concurrent {
            sql.push_str("CONCURRENTLY ");
        }
        if self.missing_ok {
            sql.push_str("IF EXISTS ");
        }

        match self.removeType {
            ObjectType::OBJECT_RULE => {
                let objects = self.objects.as_ref().unwrap();
                if let Node::List(objects) = objects.get(0).as_ref().unwrap() {
                    let tablename = objects.get(0).unwrap();
                    let rulename = objects.get(1).unwrap();
                    sql.push_str(&rulename.sql_ident());
                    sql.push_str(" ON ");
                    sql.push_str(&tablename.sql_ident());
                }
            }
            _ => {
                for (i, node) in self.objects.as_ref().unwrap().iter().enumerate() {
                    if i > 0 {
                        sql.push_str(", ");
                    }
                    if let Node::List(names) = node {
                        sql.push_str(&names.sql_ident());
                    } else if let Node::Value(_) = node {
                        sql.push_str(&node.sql_ident());
                    } else {
                        sql.push_str(&node.sql());
                    }
                }
            }
        }

        sql.push_str(&self.behavior.sql_prefix(" "));

        sql
    }
}

impl Diff for DropStmt {}
```

## File: `src/nodes/explain_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlList};
use postgres_parser::nodes::ExplainStmt;

impl Sql for ExplainStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("EXPLAIN ");
        sql.push_str(&self.options.sql_wrap(", ", "(", ")"));
        sql.push_str(&self.query.sql_prefix(" "));

        sql
    }
}

impl Diff for ExplainStmt {}
```

## File: `src/nodes/fetch_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlIdent};
use postgres_parser::nodes::FetchStmt;
use postgres_parser::sys::FetchDirection;

impl Sql for FetchStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("FETCH ");

        match self.direction {
            FetchDirection::FETCH_FORWARD => sql.push_str("FORWARD "),
            FetchDirection::FETCH_BACKWARD => sql.push_str("BACKWARD "),
            FetchDirection::FETCH_ABSOLUTE => sql.push_str("ABSOLUTE "),
            FetchDirection::FETCH_RELATIVE => sql.push_str("RELATIVE "),
        }

        if self.howMany == std::i64::MAX {
            sql.push_str("ALL");
        } else {
            sql.push_str(&self.howMany.to_string());
        }

        sql.push_str(" FROM ");
        sql.push_str(&self.portalname.sql_ident());

        sql
    }
}

impl Diff for FetchStmt {}
```

## File: `src/nodes/func_call.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::make_name;
use crate::schema_set::{Sql, SqlList};
use postgres_parser::nodes::FuncCall;

impl Sql for FuncCall {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str(&make_name(&self.funcname).expect("no name for FuncCall"));
        sql.push('(');
        if self.agg_star {
            sql.push('*');
        } else if self.agg_distinct {
            sql.push_str("DISTINCT ");
        }
        if self.func_variadic {
            sql.push_str("VARIADIC ");
        }
        sql.push_str(&self.args.sql(", "));
        if self.agg_within_group {
            sql.push(')');
            sql.push_str(" WITHIN GROUP (")
        }
        sql.push_str(&self.agg_order.sql_prefix(" ORDER BY ", ", "));
        sql.push(')');
        sql.push_str(&self.over.sql_prefix(" OVER"));
        sql.push_str(
            &self
                .agg_filter
                .sql_prefix_and_wrap(" FILTER", "(WHERE ", ")"),
        );
        sql
    }
}
```

## File: `src/nodes/function_parameter.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlIdent};
use postgres_parser::nodes::FunctionParameter;
use postgres_parser::sys::FunctionParameterMode;

impl Sql for FunctionParameter {
    fn sql(&self) -> String {
        let mut sql = String::new();

        match self.mode {
            FunctionParameterMode::FUNC_PARAM_IN => { /* IN is the default */ }
            FunctionParameterMode::FUNC_PARAM_INOUT => sql.push_str("INOUT "),
            FunctionParameterMode::FUNC_PARAM_OUT => sql.push_str("OUT "),
            FunctionParameterMode::FUNC_PARAM_VARIADIC => sql.push_str("VARIADIC "),
            FunctionParameterMode::FUNC_PARAM_TABLE => { /* do nothing */ }
        }

        sql.push_str(&self.name.sql_ident_suffix(" "));
        sql.push_str(&self.argType.sql());
        if let Some(default) = &self.defexpr {
            let default_value = default.sql();
            if default_value == "(('t')::bool)" || default_value == "(('t')::pg_catalog.bool)" {
                sql.push_str(" DEFAULT 'true'");
            } else if default_value == "(('f')::bool)"
                || default_value == "(('f')::pg_catalog.bool)"
            {
                sql.push_str(" DEFAULT 'false'");
            } else if default_value == "NULL" {
                sql.push_str(" DEFAULT NULL");
            } else if default_value.starts_with("'") && default_value.ends_with("'") {
                sql.push_str(&self.defexpr.sql_prefix(" DEFAULT "));
            } else {
                sql.push_str(&format!(" DEFAULT '{}'", default_value));
            }
        }

        sql
    }
}
```

## File: `src/nodes/grant_role_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlList};
use postgres_parser::nodes::GrantRoleStmt;

impl Sql for GrantRoleStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str(if self.is_grant { "GRANT " } else { "REVOKE " });

        sql.push_str(&self.granted_roles.sql(", "));
        sql.push_str(" TO ");
        sql.push_str(&self.grantee_roles.sql(", "));

        if self.admin_opt {
            sql.push_str(" WITH ADMIN OPTION")
        }

        sql.push_str(&self.grantor.sql_prefix(" GRANTED BY "));

        sql
    }
}

impl Diff for GrantRoleStmt {}
```

## File: `src/nodes/grant_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlList};
use postgres_parser::nodes::GrantStmt;
use postgres_parser::sys::GrantTargetType;

impl Sql for GrantStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str(if self.is_grant { "GRANT " } else { "REVOKE " });
        if self.privileges.is_none() {
            sql.push_str("ALL PRIVILEGES")
        } else {
            sql.push_str(&self.privileges.sql(", "));
        }

        sql.push_str(" ON ");
        match self.targtype {
            GrantTargetType::ACL_TARGET_OBJECT => sql.push_str(&self.objtype.sql()),
            GrantTargetType::ACL_TARGET_ALL_IN_SCHEMA => {
                sql.push_str(&format!("ALL {}S IN SCHEMA", self.objtype.sql()))
            }
            GrantTargetType::ACL_TARGET_DEFAULTS => {
                unimplemented!("GrantTargetType::ACL_TARGET_DEFAULTS")
            }
        }

        sql.push(' ');

        sql.push_str(&self.objects.sql(", "));
        sql.push_str(" TO ");
        sql.push_str(&self.grantees.sql(", "));

        if self.grant_option {
            sql.push_str(" WITH GRANT OPTION");
        }

        sql
    }
}

impl Diff for GrantStmt {}
```

## File: `src/nodes/index_elem.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlIdent, SqlList};
use postgres_parser::nodes::IndexElem;

impl Sql for IndexElem {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str(&self.expr.sql_wrap("(", ")"));
        sql.push_str(&self.name.sql_ident());
        sql.push(' ');
        sql.push_str(
            &self
                .collation
                .sql_prefix_and_wrap(" COLLATE ", "\"", "\"", ""),
        );
        sql.push_str(&self.opclass.sql_prefix(" ", ""));
        sql.push_str(&self.ordering.sql_prefix(" "));
        sql.push_str(&self.nulls_ordering.sql_prefix(" "));

        sql
    }
}
```

## File: `src/nodes/index_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlIdent, SqlList};
use postgres_parser::nodes::IndexStmt;

impl Sql for IndexStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("CREATE ");
        if self.unique {
            sql.push_str("UNIQUE ");
        }
        sql.push_str("INDEX ");
        if self.concurrent {
            sql.push_str("CONCURRENTLY ");
        }
        if self.if_not_exists {
            sql.push_str("IF NOT EXISTS ");
        }
        sql.push_str(&self.idxname.sql_ident());
        sql.push_str(" ON ");
        if !self.relation.as_ref().unwrap().inh {
            sql.push_str("ONLY ");
        }
        sql.push_str(&self.relation.sql());
        sql.push_str(" USING ");
        sql.push_str(&self.accessMethod.sql_ident());
        sql.push_str(&self.indexParams.sql_wrap(", ", "(", ")"));
        sql.push_str(
            &self
                .indexIncludingParams
                .sql_prefix_and_wrap(" INCLUDE", "(", ")", ", "),
        );
        sql.push_str(&self.options.sql_prefix_and_wrap(" WITH ", "(", ")", ", "));
        sql.push_str(&self.tableSpace.sql_ident_prefix(" TABLESPACE "));
        sql.push_str(&self.whereClause.sql_prefix(" WHERE "));

        sql
    }
}

impl Diff for IndexStmt {}
```

## File: `src/nodes/infer_clause.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Len, Sql, SqlIdent, SqlList};
use postgres_parser::nodes::InferClause;

impl Sql for InferClause {
    fn sql(&self) -> String {
        let mut sql = String::new();

        if self.indexElems.len() > 0 {
            sql.push_str(&self.indexElems.sql_wrap(", ", "(", ")"));
        }

        if self.whereClause.is_some() {
            sql.push_str(" WHERE ");
            sql.push_str(&self.whereClause.sql());
        }

        if self.conname.is_some() {
            sql.push_str(" ON CONSTRAINT ");
            sql.push_str(&self.conname.sql_ident());
        }

        sql
    }
}
```

## File: `src/nodes/insert_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::nodes::res_target::{res_target_insert, res_target_returning};
use crate::schema_set::{Diff, Sql};
use postgres_parser::nodes::InsertStmt;

impl Sql for InsertStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str(&self.withClause.sql());

        sql.push_str("INSERT INTO ");
        sql.push_str(&self.relation.sql());

        sql.push_str(&res_target_insert(&self.cols));

        sql.push(' ');

        if self.selectStmt.is_some() {
            sql.push_str(&self.selectStmt.sql());
        } else {
            sql.push_str("DEFAULT VALUES");
        }

        sql.push_str(&self.onConflictClause.sql());
        sql.push_str(&res_target_returning(&self.returningList));

        sql
    }
}

impl Diff for InsertStmt {
    fn drop_stmt(&self) -> Option<String> {
        None
    }
}
```

## File: `src/nodes/into_clause.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlIdent, SqlList};
use postgres_parser::nodes::IntoClause;

impl Sql for IntoClause {
    fn sql(&self) -> String {
        let mut sql = String::new();

        if self.rel.as_ref().unwrap().relpersistence == 't' {
            sql.push_str("TEMP ");
        }

        sql.push_str(&self.rel.sql());
        sql.push_str(&self.colNames.sql_wrap(", ", "(", ") "));
        sql.push_str(&self.accessMethod.sql_ident_prefix(" USING "));
        sql.push_str(&self.options.sql_prefix_and_wrap(" WITH", "(", ") ", ", "));
        sql.push_str(&self.onCommit.sql());
        sql.push_str(&self.tableSpaceName.sql_ident_prefix(" TABLESPACE "));
        sql.push_str(&self.viewQuery.sql_prefix(" AS "));

        sql
    }
}
```

## File: `src/nodes/join_expr.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlList};
use postgres_parser::nodes::JoinExpr;
use postgres_parser::sys::JoinType;

impl Sql for JoinExpr {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str(&self.larg.sql());
        match self.jointype {
            JoinType::JOIN_INNER => sql.push_str(" INNER JOIN "),
            JoinType::JOIN_LEFT => sql.push_str(" LEFT JOIN "),
            JoinType::JOIN_FULL => sql.push_str(" FULL JOIN "),
            JoinType::JOIN_RIGHT => sql.push_str(" RIGHT JOIN "),
            JoinType::JOIN_SEMI => {}
            JoinType::JOIN_ANTI => {}
            JoinType::JOIN_UNIQUE_OUTER => {}
            JoinType::JOIN_UNIQUE_INNER => {}
        }
        sql.push_str(&self.rarg.sql());
        sql.push_str(&self.alias.sql());
        sql.push_str(
            &self
                .usingClause
                .sql_prefix_and_wrap(" USING ", "(", ")", ""),
        );
        sql.push_str(&self.quals.sql_prefix(" ON "));

        sql
    }
}
```

## File: `src/nodes/listen_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlIdent};
use postgres_parser::nodes::ListenStmt;

impl Sql for ListenStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("LISTEN ");
        sql.push_str(&self.conditionname.sql_ident());

        sql
    }
}

impl Diff for ListenStmt {}
```

## File: `src/nodes/lock_stmt.rs`
```rust
use crate::schema_set::{Diff, Sql, SqlList};
use postgres_parser::nodes::LockStmt;

impl Sql for LockStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("LOCK TABLE ");
        if self.relations.is_none() {
            sql.push('*');
        } else {
            sql.push_str(&self.relations.sql(", "));
        }

        sql.push_str(" IN ");

        /*
        /* NoLock is not a lock mode, but a flag value meaning "don't get a lock" */
        #define NoLock					0

        #define AccessShareLock			1	/* SELECT */
        #define RowShareLock			2	/* SELECT FOR UPDATE/FOR SHARE */
        #define RowExclusiveLock		3	/* INSERT, UPDATE, DELETE */
        #define ShareUpdateExclusiveLock 4	/* VACUUM (non-FULL),ANALYZE, CREATE INDEX
                                             * CONCURRENTLY */
        #define ShareLock				5	/* CREATE INDEX (WITHOUT CONCURRENTLY) */
        #define ShareRowExclusiveLock	6	/* like EXCLUSIVE MODE, but allows ROW
                                             * SHARE */
        #define ExclusiveLock			7	/* blocks ROW SHARE/SELECT...FOR UPDATE */
        #define AccessExclusiveLock		8	/* ALTER TABLE, DROP TABLE, VACUUM FULL,
                                             * and unqualified LOCK TABLE */

                 */
        match self.mode {
            1 => sql.push_str("ACCESS SHARE"),
            2 => sql.push_str("ROW SHARE"),
            3 => sql.push_str("ROW EXCLUSIVE"),
            4 => sql.push_str("SHARE UPDATE EXCLUSIVE"),
            5 => sql.push_str("SHARE"),
            6 => sql.push_str("SHARE ROW EXCLUSIVE"),
            7 => sql.push_str("EXCLUSIVE"),
            8 => sql.push_str("ACCESS EXCLUSIVE"),
            _ => panic!("unrecognized lock mode"),
        }

        sql.push_str(" MODE");
        if self.nowait {
            sql.push_str(" NOWAIT");
        }

        sql
    }
}

impl Diff for LockStmt {}
```

## File: `src/nodes/locking_clause.rs`
```rust
use crate::schema_set::{Sql, SqlList};
use postgres_parser::nodes::LockingClause;
use postgres_parser::sys::{LockClauseStrength, LockWaitPolicy};

impl Sql for LockingClause {
    fn sql(&self) -> String {
        let mut sql = String::new();

        match self.strength {
            LockClauseStrength::LCS_NONE => {}
            LockClauseStrength::LCS_FORKEYSHARE => sql.push_str(" FOR KEY SHARE"),
            LockClauseStrength::LCS_FORSHARE => sql.push_str(" FOR SHARE"),
            LockClauseStrength::LCS_FORNOKEYUPDATE => sql.push_str(" FOR NO KEY UPDATE"),
            LockClauseStrength::LCS_FORUPDATE => sql.push_str(" FOR UPDATE"),
        }

        sql.push_str(&self.lockedRels.sql_prefix(" OF ", ", "));

        match self.waitPolicy {
            LockWaitPolicy::LockWaitBlock => {}
            LockWaitPolicy::LockWaitSkip => sql.push_str(" SKIP LOCKED"),
            LockWaitPolicy::LockWaitError => sql.push_str(" NOWAIT"),
        }

        sql
    }
}
```

## File: `src/nodes/min_max_expr.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlList};
use postgres_parser::nodes::MinMaxExpr;
use postgres_parser::sys::MinMaxOp;

impl Sql for MinMaxExpr {
    fn sql(&self) -> String {
        match self.op {
            MinMaxOp::IS_GREATEST => format!("greatest({})", self.args.sql(", ")),
            MinMaxOp::IS_LEAST => format!("least({})", self.args.sql(", ")),
        }
    }
}
```

## File: `src/nodes/mod.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlIdent};
use postgres_parser::Node;

mod a_arrayexpr;
mod a_const;
mod a_expr;
mod a_indicies;
mod a_indirection;
mod a_star;
mod access_priv;
mod alias;
mod alter_collation_stmt;
mod alter_function_stmt;
mod alter_object_schema_stmt;
mod alter_owner_stmt;
mod alter_table_cmd;
mod alter_table_stmt;
mod alter_type_stmt;
mod bool_expr;
mod boolean_test;
mod case_expr;
mod case_when;
mod cluster_stmt;
mod cmd_type;
mod coalesce_expr;
mod coercion_context;
mod collate_clause;
mod column_def;
mod column_ref;
mod comment_stmt;
mod common_table_expr;
mod composite_type_stmt;
mod constraint;
mod copy_stmt;
mod create_am_stmt;
mod create_cast_stmt;
mod create_conversion_stmt;
mod create_domain_stmt;
mod create_enum_stmt;
mod create_event_trig_stmt;
mod create_fdw_stmt;
mod create_foreign_server_stmt;
mod create_foreign_table_stmt;
mod create_function_stmt;
mod create_op_class_item;
mod create_op_class_stmt;
mod create_policy_stmt;
mod create_range_stmt;
mod create_role_stmt;
mod create_schema_stmt;
mod create_seq_stmt;
mod create_stmt;
mod create_table_as_stmt;
mod create_trig_stmt;
mod current_of_expr;
mod declare_cursor_stmt;
mod def_elem;
mod define_stmt;
mod delete_stmt;
mod discard_stmt;
mod do_stmt;
mod drop_behavior;
mod drop_role_stmt;
mod drop_stmt;
mod explain_stmt;
mod fetch_stmt;
mod func_call;
mod function_parameter;
mod grant_role_stmt;
mod grant_stmt;
mod index_elem;
mod index_stmt;
mod infer_clause;
mod insert_stmt;
mod into_clause;
mod join_expr;
mod listen_stmt;
mod lock_stmt;
mod locking_clause;
mod min_max_expr;
mod multi_assign_ref;
mod notify_stmt;
mod null_test;
mod object_type;
mod object_with_args;
mod on_commit_action;
mod on_conflict_clause;
mod partition_bound_spec;
mod partition_elem;
mod partition_spec;
mod prepare_stmt;
mod range_function;
mod range_subselect;
mod range_var;
mod rename_stmt;
mod res_target;
mod role_spec;
mod row_expr;
mod rule_stmt;
mod select_stmt;
mod set_to_default;
mod sort_by;
mod sort_by_dir;
mod sort_by_nulls;
mod sql_value_function;
mod sub_link;
mod table_like_clause;
mod transaction_stmt;
mod truncate_stmt;
mod type_cast;
mod type_name;
mod unlisten_stmt;
mod update_stmt;
mod vacuum_relation;
mod vacuum_stmt;
mod value;
mod variable_set_stmt;
mod variable_show_stmt;
mod vec_of_node;
mod view_check_option;
mod view_stmt;
mod window_def;
mod with_clause;

impl Sql for Node {
    #[track_caller]
    fn sql(&self) -> String {
        match self {
            Node::A_ArrayExpr(stmt) => stmt.sql(),
            Node::A_Const(stmt) => stmt.sql(),
            Node::A_Expr(stmt) => stmt.sql(),
            Node::A_Indices(stmt) => stmt.sql(),
            Node::A_Indirection(stmt) => stmt.sql(),
            Node::A_Star(stmt) => stmt.sql(),
            Node::AccessPriv(stmt) => stmt.sql(),
            Node::Alias(stmt) => stmt.sql(),
            Node::AlterCollationStmt(stmt) => stmt.sql(),
            Node::AlterFunctionStmt(stmt) => stmt.sql(),
            Node::AlterObjectSchemaStmt(stmt) => stmt.sql(),
            Node::AlterOwnerStmt(stmt) => stmt.sql(),
            Node::AlterTableCmd(stmt) => stmt.sql(),
            Node::AlterTableStmt(stmt) => stmt.sql(),
            Node::AlterTypeStmt(stmt) => stmt.sql(),
            Node::BoolExpr(stmt) => stmt.sql(),
            Node::BooleanTest(stmt) => stmt.sql(),
            Node::CaseExpr(stmt) => stmt.sql(),
            Node::CaseWhen(stmt) => stmt.sql(),
            Node::ClusterStmt(stmt) => stmt.sql(),
            Node::CoalesceExpr(stmt) => stmt.sql(),
            Node::CollateClause(stmt) => stmt.sql(),
            Node::ColumnDef(stmt) => stmt.sql(),
            Node::ColumnRef(stmt) => stmt.sql_ident(),
            Node::CommentStmt(stmt) => stmt.sql(),
            Node::CommonTableExpr(stmt) => stmt.sql(),
            Node::CompositeTypeStmt(stmt) => stmt.sql(),
            Node::Constraint(stmt) => stmt.sql(),
            Node::CopyStmt(stmt) => stmt.sql(),
            Node::CreateAmStmt(stmt) => stmt.sql(),
            Node::CreateCastStmt(stmt) => stmt.sql(),
            Node::CreateConversionStmt(stmt) => stmt.sql(),
            Node::CreateDomainStmt(stmt) => stmt.sql(),
            Node::CreateEnumStmt(stmt) => stmt.sql(),
            Node::CreateFdwStmt(stmt) => stmt.sql(),
            Node::CreateForeignServerStmt(stmt) => stmt.sql(),
            Node::CreateForeignTableStmt(stmt) => stmt.sql(),
            Node::CreateFunctionStmt(stmt) => {
                let mut stmt = stmt.clone();
                stmt.replace = true;
                stmt.sql()
            }
            Node::CreateOpClassItem(stmt) => stmt.sql(),
            Node::CreateOpClassStmt(stmt) => stmt.sql(),
            Node::CreatePolicyStmt(stmt) => stmt.sql(),
            Node::CreateRangeStmt(stmt) => stmt.sql(),
            Node::CreateRoleStmt(stmt) => stmt.sql(),
            Node::CreateSeqStmt(stmt) => stmt.sql(),
            Node::CreateTrigStmt(stmt) => stmt.sql(),
            Node::CreateSchemaStmt(stmt) => stmt.sql(),
            Node::CreateStmt(stmt) => stmt.sql(),
            Node::CreateTableAsStmt(stmt) => stmt.sql(),
            Node::CurrentOfExpr(stmt) => stmt.sql(),
            Node::DeclareCursorStmt(stmt) => stmt.sql(),
            Node::DefElem(stmt) => stmt.sql(),
            Node::DefineStmt(stmt) => stmt.sql(),
            Node::DeleteStmt(stmt) => stmt.sql(),
            Node::DiscardStmt(stmt) => stmt.sql(),
            Node::DoStmt(stmt) => stmt.sql(),
            Node::DropRoleStmt(stmt) => stmt.sql(),
            Node::DropStmt(stmt) => stmt.sql(),
            Node::ExplainStmt(node) => node.sql(),
            Node::Expr(node) => node.sql(),
            Node::FetchStmt(stmt) => stmt.sql(),
            Node::FuncCall(stmt) => stmt.sql(),
            Node::FunctionParameter(stmt) => stmt.sql(),
            Node::GrantRoleStmt(stmt) => stmt.sql(),
            Node::GrantStmt(stmt) => stmt.sql(),
            Node::IndexElem(stmt) => stmt.sql(),
            Node::IndexStmt(stmt) => stmt.sql(),
            Node::InferClause(stmt) => stmt.sql(),
            Node::InsertStmt(stmt) => stmt.sql(),
            Node::IntoClause(stmt) => stmt.sql(),
            Node::JoinExpr(stmt) => stmt.sql(),
            Node::List(_) => String::new(),
            Node::ListenStmt(stmt) => stmt.sql(),
            Node::LockStmt(stmt) => stmt.sql(),
            Node::LockingClause(stmt) => stmt.sql(),
            Node::MultiAssignRef(stmt) => stmt.sql(),
            Node::NotifyStmt(stmt) => stmt.sql(),
            Node::NullTest(stmt) => stmt.sql(),
            Node::MinMaxExpr(stmt) => stmt.sql(),
            Node::ObjectWithArgs(stmt) => stmt.sql(),
            Node::OnConflictClause(stmt) => stmt.sql(),
            Node::PartitionBoundSpec(stmt) => stmt.sql(),
            Node::PartitionElem(stmt) => stmt.sql(),
            Node::PartitionSpec(stmt) => stmt.sql(),
            Node::PrepareStmt(stmt) => stmt.sql(),
            Node::RangeFunction(stmt) => stmt.sql(),
            Node::RangeSubselect(stmt) => stmt.sql(),
            Node::RangeVar(stmt) => stmt.sql(),
            Node::RenameStmt(stmt) => stmt.sql(),
            Node::ResTarget(_) => unreachable!("encountered a ResTarget node"),
            Node::RoleSpec(stmt) => stmt.sql(),
            Node::RuleStmt(stmt) => stmt.sql(),
            Node::RowExpr(stmt) => stmt.sql(),
            Node::SelectStmt(stmt) => stmt.sql(),
            Node::SetToDefault(stmt) => stmt.sql(),
            Node::SortBy(stmt) => stmt.sql(),
            Node::SQLValueFunction(stmt) => stmt.sql(),
            Node::SubLink(stmt) => stmt.sql(),
            Node::TableLikeClause(stmt) => stmt.sql(),
            Node::TransactionStmt(stmt) => stmt.sql(),
            Node::TruncateStmt(stmt) => stmt.sql(),
            Node::TypeCast(stmt) => stmt.sql(),
            Node::TypeName(stmt) => stmt.sql(),
            Node::UnlistenStmt(stmt) => stmt.sql(),
            Node::UpdateStmt(stmt) => stmt.sql(),
            Node::VacuumRelation(stmt) => stmt.sql(),
            Node::VacuumStmt(stmt) => stmt.sql(),
            Node::Value(stmt) => stmt.sql(),
            Node::VariableSetStmt(stmt) => stmt.sql(),
            Node::VariableShowStmt(stmt) => stmt.sql(),
            Node::ViewStmt(stmt) => stmt.sql(),
            Node::WindowDef(stmt) => stmt.sql(),
            Node::WithClause(stmt) => stmt.sql(),
            Node::CreateEventTrigStmt(stmt) => stmt.sql(),

            _ => unimplemented!("Node: {:?}", self),
        }
    }
}
```

## File: `src/nodes/multi_assign_ref.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Len, Sql};
use postgres_parser::nodes::MultiAssignRef;
use postgres_parser::Node;

impl Sql for MultiAssignRef {
    fn sql(&self) -> String {
        let mut sql = String::new();

        match self.source.as_ref() {
            None => {}
            Some(source) => match source.as_ref() {
                Node::RowExpr(row_expr) if row_expr.args.len() > 0 => {
                    sql.push_str(&row_expr.args.as_ref().unwrap()[self.colno as usize - 1].sql())
                }
                Node::SubLink(sub_link) => sql.push_str(&sub_link.sql()),
                _ => panic!(
                    "unexpected 'source' node in MultiAssignRef: {:?}",
                    self.source
                ),
            },
        }
        if let Some(_vec) = self.source.as_ref() {
            // sql.push_str(&vec[self.colno as usize].sql());
        }

        sql
    }
}
```

## File: `src/nodes/notify_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlIdent};
use postgres_parser::nodes::NotifyStmt;

impl Sql for NotifyStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str(&self.conditionname.sql_ident_prefix("NOTIFY "));
        if self.payload.is_some() {
            sql.push_str(&format!(
                ", '{}'",
                self.payload.as_ref().unwrap().replace("'", "''")
            ));
        }

        sql
    }
}

impl Diff for NotifyStmt {}
```

## File: `src/nodes/null_test.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::Sql;
use postgres_parser::nodes::NullTest;
use postgres_parser::sys::NullTestType;

impl Sql for NullTestType {
    fn sql(&self) -> String {
        match self {
            NullTestType::IS_NULL => "IS NULL",
            NullTestType::IS_NOT_NULL => "IS NOT NULL",
        }
        .into()
    }
}

impl Sql for NullTest {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push('(');
        sql.push_str(&self.arg.sql());
        sql.push(')');
        sql.push(' ');
        sql.push_str(&self.nulltesttype.sql());

        sql
    }
}
```

## File: `src/nodes/object_type.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::Sql;
use postgres_parser::sys::ObjectType;

impl Sql for ObjectType {
    fn sql(&self) -> String {
        match self {
            ObjectType::OBJECT_ACCESS_METHOD => "ACCESS METHOD",
            ObjectType::OBJECT_AGGREGATE => "AGGREGATE",
            ObjectType::OBJECT_AMOP => "AMOP",
            ObjectType::OBJECT_AMPROC => "AMPROC",
            ObjectType::OBJECT_ATTRIBUTE => "ATTRIBUTE",
            ObjectType::OBJECT_CAST => "CAST",
            ObjectType::OBJECT_COLUMN => "COLUMN",
            ObjectType::OBJECT_COLLATION => "COLLATION",
            ObjectType::OBJECT_CONVERSION => "CONVERSION",
            ObjectType::OBJECT_DATABASE => "DATABASE",
            ObjectType::OBJECT_DEFAULT => "DEFAULT",
            ObjectType::OBJECT_DEFACL => "DEFACL",
            ObjectType::OBJECT_DOMAIN => "DOMAIN",
            ObjectType::OBJECT_DOMCONSTRAINT => "DOMCONSTRAINT",
            ObjectType::OBJECT_EVENT_TRIGGER => "EVENT TRIGGER",
            ObjectType::OBJECT_EXTENSION => "EXTENSION",
            ObjectType::OBJECT_FDW => "FDW",
            ObjectType::OBJECT_FOREIGN_SERVER => "FOREIGN SERVER",
            ObjectType::OBJECT_FOREIGN_TABLE => "FOREIGN TABLE",
            ObjectType::OBJECT_FUNCTION => "FUNCTION",
            ObjectType::OBJECT_INDEX => "INDEX",
            ObjectType::OBJECT_LANGUAGE => "LANGUAGE",
            ObjectType::OBJECT_LARGEOBJECT => "LARGEOBJECT",
            ObjectType::OBJECT_MATVIEW => "MATERIALIZED VIEW",
            ObjectType::OBJECT_OPCLASS => "OPCLASS",
            ObjectType::OBJECT_OPERATOR => "OPERATOR",
            ObjectType::OBJECT_OPFAMILY => "OPFAMILY",
            ObjectType::OBJECT_POLICY => "POLICY",
            ObjectType::OBJECT_PROCEDURE => "PROCEDURE",
            ObjectType::OBJECT_PUBLICATION => "PUBLICATION",
            ObjectType::OBJECT_PUBLICATION_REL => "PUBLICATION REL",
            ObjectType::OBJECT_ROLE => "ROLE",
            ObjectType::OBJECT_ROUTINE => "ROUTINE",
            ObjectType::OBJECT_RULE => "RULE",
            ObjectType::OBJECT_SCHEMA => "SCHEMA",
            ObjectType::OBJECT_SEQUENCE => "SEQUENCE",
            ObjectType::OBJECT_SUBSCRIPTION => "SUBSCRIPTION",
            ObjectType::OBJECT_STATISTIC_EXT => "STATISTIC EXT",
            ObjectType::OBJECT_TABCONSTRAINT => "TABCONSTRAINT",
            ObjectType::OBJECT_TABLE => "TABLE",
            ObjectType::OBJECT_TABLESPACE => "TABLESPACE",
            ObjectType::OBJECT_TRANSFORM => "TRANSFORM",
            ObjectType::OBJECT_TRIGGER => "TRIGGER",
            ObjectType::OBJECT_TSCONFIGURATION => "TSCONFIGURATION",
            ObjectType::OBJECT_TSDICTIONARY => "TSDICTIONARY",
            ObjectType::OBJECT_TSPARSER => "TSPARSER",
            ObjectType::OBJECT_TSTEMPLATE => "TSTEMPLATE",
            ObjectType::OBJECT_TYPE => "TYPE",
            ObjectType::OBJECT_USER_MAPPING => "USER MAPPING",
            ObjectType::OBJECT_VIEW => "VIEW",
        }
        .into()
    }
}
```

## File: `src/nodes/object_with_args.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlIdent, SqlList};
use postgres_parser::nodes::ObjectWithArgs;

impl Sql for ObjectWithArgs {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str(&self.objname.sql_ident());

        if !self.args_unspecified && self.objargs.is_none() {
            // noop
        } else {
            if !self.args_unspecified {
                sql.push('(');
                if self.objargs.is_none() {
                    sql.push('*');
                } else {
                    sql.push_str(&self.objargs.sql(", "));
                }
                sql.push(')');
            }
        }

        sql
    }
}
```

## File: `src/nodes/on_commit_action.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::Sql;
use postgres_parser::sys::OnCommitAction;

impl Sql for OnCommitAction {
    fn sql(&self) -> String {
        match self {
            OnCommitAction::ONCOMMIT_NOOP => "",
            OnCommitAction::ONCOMMIT_PRESERVE_ROWS => "ON COMMIT PRESERVE ROWS ",
            OnCommitAction::ONCOMMIT_DELETE_ROWS => "ON COMMIT DELETE ROWS ",
            OnCommitAction::ONCOMMIT_DROP => "ON COMMIT DROP ",
        }
        .into()
    }
}
```

## File: `src/nodes/on_conflict_clause.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlIdent, SqlList};
use postgres_parser::nodes::OnConflictClause;
use postgres_parser::sys::OnConflictAction;
use postgres_parser::Node;

impl Sql for OnConflictClause {
    fn sql(&self) -> String {
        match self.action {
            OnConflictAction::ONCONFLICT_NONE => "".into(),
            OnConflictAction::ONCONFLICT_NOTHING | OnConflictAction::ONCONFLICT_UPDATE => {
                let mut sql = String::new();

                sql.push_str(" ON CONFLICT ");
                sql.push_str(&self.infer.sql());

                if self.whereClause.is_some() {
                    unimplemented!("don't know how to handle 'whereClause' for OnConflictClause");
                }

                match self.action {
                    OnConflictAction::ONCONFLICT_NOTHING => sql.push_str(" DO NOTHING"),
                    OnConflictAction::ONCONFLICT_UPDATE => sql.push_str(" DO UPDATE"),
                    _ => {}
                }

                if let Some(target_list) = &self.targetList {
                    sql.push_str(" SET ");
                    let mut i = 0;
                    for node in target_list {
                        match node {
                            Node::ResTarget(res_target) => {
                                if i > 0 {
                                    sql.push_str(", ");
                                }
                                sql.push_str(&res_target.name.sql_ident());
                                sql.push_str(
                                    &res_target.indirection.sql_wrap_each(Some("["), Some("]")),
                                );
                                sql.push_str(" = ");
                                sql.push_str(&res_target.val.sql());
                                i += 1;
                            }

                            _ => panic!("unexpected node in 'targetList' of OnConflictClause"),
                        }
                    }
                }

                if self.whereClause.is_some() {
                    sql.push_str(" WHERE ");
                    sql.push_str(&self.whereClause.sql());
                }

                sql
            }
        }
    }
}
```

## File: `src/nodes/partition_bound_spec.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlList};
use postgres_parser::nodes::PartitionBoundSpec;

impl Sql for PartitionBoundSpec {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("FOR VALUES ");
        match self.strategy {
            'h' => {
                sql.push_str("WITH (");
                sql.push_str("MODULUS ");
                sql.push_str(&self.modulus.to_string());
                sql.push_str(", ");
                sql.push_str("REMAINDER ");
                sql.push_str(&self.remainder.to_string());
                sql.push(')');
            }

            'l' => {
                sql.push_str(&self.listdatums.sql_prefix_and_wrap("IN ", "(", ")", ", "));
            }

            'r' => {
                sql.push_str("FROM (");
                sql.push_str(&self.lowerdatums.sql(", "));
                sql.push(')');
                sql.push_str(" TO (");
                sql.push_str(&self.upperdatums.sql(", "));
                sql.push(')');
            }

            _ => panic!(
                "unsupported PartitionBoundSpec::strategy: `{}`",
                self.strategy
            ),
        }

        sql
    }
}
```

## File: `src/nodes/partition_elem.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlIdent};
use postgres_parser::nodes::PartitionElem;

impl Sql for PartitionElem {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str(&self.name.sql_ident());
        sql.push_str(&self.expr.sql());
        sql.push_str(&self.collation.sql_ident());
        sql.push_str(&self.opclass.sql_ident());

        sql
    }
}
```

## File: `src/nodes/partition_spec.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlList};
use postgres_parser::nodes::PartitionSpec;

impl Sql for PartitionSpec {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str(&self.strategy.as_ref().unwrap());
        sql.push_str(&self.partParams.sql_wrap(", ", "(", ")"));

        sql
    }
}
```

## File: `src/nodes/prepare_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Len, Sql, SqlIdent, SqlList};
use postgres_parser::nodes::PrepareStmt;

impl Sql for PrepareStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("PREPARE ");

        sql.push_str(&self.name.sql_ident());
        if self.argtypes.len() > 0 {
            sql.push_str(&self.argtypes.sql(", "))
        }

        sql.push_str(" AS ");
        sql.push_str(&self.query.sql());

        sql
    }
}

impl Diff for PrepareStmt {}
```

## File: `src/nodes/range_function.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlList};
use postgres_parser::nodes::RangeFunction;

impl Sql for RangeFunction {
    fn sql(&self) -> String {
        let mut sql = String::new();

        if self.lateral {
            sql.push_str("LATERAL ");
        }

        sql.push_str(&self.functions.sql(", "));
        if self.ordinality {
            sql.push_str("WITH ORDINALITY ");
        }
        sql.push_str(&self.alias.sql());

        sql
    }
}
```

## File: `src/nodes/range_subselect.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::Sql;
use postgres_parser::nodes::RangeSubselect;

impl Sql for RangeSubselect {
    fn sql(&self) -> String {
        let mut sql = String::new();

        if self.lateral {
            sql.push_str("LATERAL ");
        }
        sql.push_str(&self.subquery.sql_wrap("(", ")"));
        sql.push_str(&self.alias.sql());

        sql
    }
}
```

## File: `src/nodes/range_var.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlIdent};
use postgres_parser::nodes::RangeVar;

impl Sql for RangeVar {
    fn sql(&self) -> String {
        let mut sql = String::new();

        if !self.inh {
            sql.push_str("ONLY ");
        }
        sql.push_str(&self.catalogname.sql_ident_suffix("."));
        sql.push_str(&self.schemaname.sql_ident_suffix("."));
        sql.push_str(&self.relname.sql_ident());
        sql.push_str(&self.alias.sql());

        sql
    }
}
```

## File: `src/nodes/rename_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlIdent, SqlMaybeList};
use postgres_parser::nodes::RenameStmt;

impl Sql for RenameStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("ALTER ");
        sql.push_str(&self.renameType.sql());
        sql.push(' ');
        sql.push_str(&self.object.sql_maybe_list("."));
        sql.push_str(" RENAME TO ");
        sql.push_str(&self.newname.sql_ident());

        sql
    }
}

impl Diff for RenameStmt {}
```

## File: `src/nodes/res_target.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlIdent};
use crate::EMPTY_NODE_VEC;

use crate::nodes::a_indirection::indirection_list;
use postgres_parser::Node;

pub fn res_target_select(targets: &Option<Vec<Node>>) -> String {
    let mut sql = String::new();

    for (i, node) in targets
        .as_ref()
        .unwrap_or(&EMPTY_NODE_VEC)
        .iter()
        .enumerate()
    {
        if let Node::ResTarget(node) = node {
            if i > 0 {
                sql.push_str(", ");
            }

            sql.push_str(&node.val.sql());
            sql.push_str(&indirection_list(&node.indirection));
            if node.name.is_some() {
                sql.push_str(" AS ");
                sql.push_str(&node.name.sql_ident());
            }
        } else {
            panic!("unexpected node: {:?}", node);
        }
    }

    sql
}

pub fn res_target_insert(targets: &Option<Vec<Node>>) -> String {
    match targets {
        None => String::new(),
        Some(targets) => {
            let mut sql = String::new();

            sql.push('(');
            for (i, node) in targets.iter().enumerate() {
                if let Node::ResTarget(node) = node {
                    if i > 0 {
                        sql.push_str(", ");
                    }

                    sql.push_str(&node.name.sql_ident());
                    sql.push_str(&indirection_list(&node.indirection));
                } else {
                    panic!("unexpected node: {:?}", node);
                }
            }
            sql.push(')');

            sql
        }
    }
}

pub fn res_target_update(targets: &Option<Vec<Node>>) -> String {
    let mut sql = String::new();

    let mut iter = targets
        .as_ref()
        .unwrap_or(&EMPTY_NODE_VEC)
        .iter()
        .map(|n| match n {
            Node::ResTarget(ref res_target) => res_target,
            unexpected => panic!("unexpected node in update targetList: {unexpected:?}"),
        });

    let mut i = 0;
    loop {
        let mut current = iter.next();

        if current.is_none() {
            break;
        }
        let mut mars = Vec::new();
        while let Node::MultiAssignRef(multi_assign_ref) =
            current.as_ref().unwrap().val.as_ref().unwrap().as_ref()
        {
            mars.push((multi_assign_ref, current.unwrap()));
            current = iter.next();
            if current.is_none() {
                break;
            }
        }

        if i > 0 {
            sql.push_str(", ");
        }
        let current_i = i;
        if !mars.is_empty() {
            sql.push('(');
            for (_, res_target) in &mars {
                if i > 0 && i > current_i {
                    sql.push_str(", ");
                }
                sql.push_str(&res_target.name.sql_ident());
                sql.push_str(&indirection_list(&res_target.indirection));
                i += 1;
            }
            sql.push_str(") = ");

            sql.push_str(&mars[0].0.source.sql());
        }

        if let Some(node) = current {
            if i > 0 && i > current_i {
                sql.push_str(", ");
            }
            sql.push_str(&node.name.sql_ident());
            sql.push_str(&indirection_list(&node.indirection));
            sql.push_str(" = ");
            sql.push_str(&node.val.sql());

            i += 1;
        }
    }

    sql
}

pub fn res_target_returning(targets: &Option<Vec<Node>>) -> String {
    match targets {
        None => String::new(),
        Some(targets) => {
            let mut sql = String::new();

            sql.push_str(" RETURNING ");

            for (i, node) in targets.iter().enumerate() {
                if let Node::ResTarget(node) = node {
                    if i > 0 {
                        sql.push_str(", ");
                    }

                    sql.push_str(&node.val.sql());

                    if node.name.is_some() {
                        sql.push_str(" AS ");
                        sql.push_str(&node.name.sql_ident());
                    }
                } else {
                    panic!("unexpected node {:?}", node);
                }
            }

            sql
        }
    }
}
```

## File: `src/nodes/role_spec.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlIdent};
use postgres_parser::nodes::RoleSpec;
use postgres_parser::sys::RoleSpecType;

impl Sql for RoleSpec {
    fn sql(&self) -> String {
        let mut sql = String::new();
        match self.roletype {
            RoleSpecType::ROLESPEC_CSTRING => sql.push_str(&self.rolename.sql_ident()),
            RoleSpecType::ROLESPEC_CURRENT_USER => sql.push_str("CURRENT_USER"),
            RoleSpecType::ROLESPEC_SESSION_USER => sql.push_str("SESSION_USER"),
            RoleSpecType::ROLESPEC_PUBLIC => sql.push_str("public"),
        }

        sql
    }
}
```

## File: `src/nodes/row_expr.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlList};
use postgres_parser::nodes::RowExpr;
use postgres_parser::sys::CoercionForm;

impl Sql for RowExpr {
    fn sql(&self) -> String {
        let mut sql = String::new();

        match self.row_format {
            CoercionForm::COERCE_EXPLICIT_CALL => sql.push_str("ROW "),
            CoercionForm::COERCE_EXPLICIT_CAST => sql.push_str("ROW "),
            CoercionForm::COERCE_IMPLICIT_CAST => {}
        }

        sql.push_str(&self.args.sql_wrap(", ", "(", ")"));

        sql
    }
}
```

## File: `src/nodes/rule_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Len, Sql, SqlIdent, SqlList};
use postgres_parser::nodes::RuleStmt;

impl Sql for RuleStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("CREATE ");
        if self.replace {
            sql.push_str("OR REPLACE ");
        }
        sql.push_str("RULE ");

        sql.push_str(&self.rulename.sql_ident());
        sql.push_str(" AS ON ");
        sql.push_str(&self.event.sql());
        sql.push_str(" TO ");
        sql.push_str(&self.relation.sql());

        sql.push_str(&self.whereClause.sql_prefix(" WHERE "));
        sql.push_str(" DO ");
        if self.instead {
            sql.push_str("INSTEAD ");
        } else {
            sql.push_str("ALSO ");
        }

        if self.actions.is_none() {
            sql.push_str("NOTHING");
        } else if self.actions.len() == 1 {
            sql.push_str(&self.actions.sql(""));
        } else {
            sql.push_str(&self.actions.sql_wrap("; ", "(", ")"))
        }

        sql
    }
}

impl Diff for RuleStmt {}
```

## File: `src/nodes/select_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::nodes::res_target::res_target_select;
use crate::schema_set::{Diff, Sql, SqlList};

use postgres_parser::nodes::SelectStmt;
use postgres_parser::sys::SetOperation;

impl Sql for SelectStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str(&self.withClause.sql());
        if let Some(values_list) = self.valuesLists.as_ref() {
            sql.push_str("VALUES ");
            sql.push_str(&values_list.sql_wrap_each_and_separate(", ", "(", ")"));
        } else if self.larg.is_some() {
            sql.push_str(&self.larg.sql());
            sql.push(' ');
        } else {
            sql.push_str("SELECT ");
            sql.push_str(&self.distinctClause.sql_prefix(" DISTINCT ", ", "));
            sql.push_str(&res_target_select(&self.targetList));
            sql.push_str(&self.intoClause.sql_prefix(" INTO "));
            sql.push_str(&self.fromClause.sql_prefix(" FROM ", ", "));
            sql.push_str(&self.whereClause.sql_prefix(" WHERE "));
            sql.push_str(&self.groupClause.sql_prefix(" GROUP BY ", ", "));
            sql.push_str(&self.havingClause.sql_prefix(" HAVING "));
            sql.push_str(&self.windowClause.sql_prefix(" WINDOW ", ", "));
        }

        match self.op {
            SetOperation::SETOP_NONE => {}
            SetOperation::SETOP_UNION => sql.push_str("UNION "),
            SetOperation::SETOP_INTERSECT => sql.push_str("INTERSECT "),
            SetOperation::SETOP_EXCEPT => sql.push_str("EXCEPT "),
        }

        if self.all {
            sql.push_str("ALL ");
        }

        sql.push_str(&self.rarg.sql_wrap("(", ")"));

        sql.push_str(&self.sortClause.sql_prefix(" ORDER BY ", ", "));
        sql.push_str(&self.limitCount.sql_prefix(" LIMIT "));
        sql.push_str(&self.limitOffset.sql_prefix(" OFFSET "));
        sql.push_str(&self.lockingClause.sql(""));

        sql
    }
}

impl Diff for SelectStmt {}
```

## File: `src/nodes/set_to_default.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::Sql;
use postgres_parser::nodes::SetToDefault;

impl Sql for SetToDefault {
    fn sql(&self) -> String {
        "DEFAULT".into()
    }
}
```

## File: `src/nodes/sort_by.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::make_operator_name;
use crate::schema_set::Sql;
use postgres_parser::nodes::SortBy;
use postgres_parser::sys::SortByDir;

impl Sql for SortBy {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str(&self.node.sql());

        match self.sortby_dir {
            SortByDir::SORTBY_DEFAULT => {}
            SortByDir::SORTBY_ASC => sql.push_str(" ASC"),
            SortByDir::SORTBY_DESC => sql.push_str(" DESC"),
            SortByDir::SORTBY_USING => {
                sql.push_str(" USING ");
                sql.push_str(
                    &make_operator_name(&self.useOp)
                        .expect("failed to make 'useOp' name for SortBy"),
                );
            }
        }

        sql.push_str(&self.sortby_nulls.sql_prefix(" "));

        sql
    }
}
```

## File: `src/nodes/sort_by_dir.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::Sql;
use postgres_parser::sys::SortByDir;

impl Sql for SortByDir {
    fn sql(&self) -> String {
        match self {
            SortByDir::SORTBY_DEFAULT => "",
            SortByDir::SORTBY_ASC => "ASC",
            SortByDir::SORTBY_DESC => "DESC",
            SortByDir::SORTBY_USING => unimplemented!("SortByDir::SORTBY_USING"),
        }
        .into()
    }
}
```

## File: `src/nodes/sort_by_nulls.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::Sql;
use postgres_parser::sys::SortByNulls;

impl Sql for SortByNulls {
    fn sql(&self) -> String {
        match self {
            SortByNulls::SORTBY_NULLS_DEFAULT => String::new(),
            SortByNulls::SORTBY_NULLS_FIRST => "NULLS FIRST".into(),
            SortByNulls::SORTBY_NULLS_LAST => "NULLS LAST".into(),
        }
    }
}
```

## File: `src/nodes/sql_value_function.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::Sql;
use postgres_parser::nodes::SQLValueFunction;
use postgres_parser::sys::SQLValueFunctionOp;

impl Sql for SQLValueFunction {
    fn sql(&self) -> String {
        match self.op {
            SQLValueFunctionOp::SVFOP_CURRENT_DATE => "current_date".into(),
            SQLValueFunctionOp::SVFOP_CURRENT_TIME | SQLValueFunctionOp::SVFOP_CURRENT_TIME_N => {
                "current_time".into()
            }
            SQLValueFunctionOp::SVFOP_CURRENT_TIMESTAMP
            | SQLValueFunctionOp::SVFOP_CURRENT_TIMESTAMP_N => "current_timestamp".into(),
            SQLValueFunctionOp::SVFOP_LOCALTIME | SQLValueFunctionOp::SVFOP_LOCALTIME_N => {
                "localtime".into()
            }
            SQLValueFunctionOp::SVFOP_LOCALTIMESTAMP
            | SQLValueFunctionOp::SVFOP_LOCALTIMESTAMP_N => "localtimestamp".into(),
            SQLValueFunctionOp::SVFOP_CURRENT_ROLE => "current_role".into(),
            SQLValueFunctionOp::SVFOP_CURRENT_USER => "current_user".into(),
            SQLValueFunctionOp::SVFOP_USER => "user".into(),
            SQLValueFunctionOp::SVFOP_SESSION_USER => "session_user".into(),
            SQLValueFunctionOp::SVFOP_CURRENT_CATALOG => "current_catalog".into(),
            SQLValueFunctionOp::SVFOP_CURRENT_SCHEMA => "current_schema".into(),
        }
    }
}
```

## File: `src/nodes/sub_link.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::make_operator_name;
use crate::schema_set::{Sql, SqlIdent};
use postgres_parser::nodes::SubLink;
use postgres_parser::sys::SubLinkType;

impl Sql for SubLink {
    fn sql(&self) -> String {
        let mut sql = String::new();

        match self.subLinkType {
            SubLinkType::EXISTS_SUBLINK => {
                sql.push_str(&self.subselect.sql_wrap(" EXISTS (", ")"));
            }
            SubLinkType::ALL_SUBLINK => {
                sql.push_str(&self.testexpr.sql());
                sql.push(' ');
                sql.push_str(
                    &make_operator_name(&self.operName)
                        .expect("failed to make operator name for SubLink"),
                );
                sql.push_str(&self.subselect.sql_wrap(" ALL (", ")"));
            }
            SubLinkType::ANY_SUBLINK => {
                sql.push_str(&self.testexpr.sql());
                sql.push(' ');

                if self.operName.is_some() {
                    sql.push_str(&self.operName.sql_ident());
                    sql.push(' ');
                } else {
                    sql.push_str("IN ");
                }
                sql.push_str(&self.subselect.sql_wrap("(", ")"));
            }
            SubLinkType::ROWCOMPARE_SUBLINK => {
                sql.push_str(&self.testexpr.sql());
                sql.push(' ');
                sql.push_str(
                    &make_operator_name(&self.operName)
                        .expect("failed to make operator name for SubLink"),
                );
                sql.push_str(&self.subselect.sql_wrap("(", ")"));
            }
            SubLinkType::EXPR_SUBLINK => {
                sql.push_str(&self.subselect.sql_wrap("(", ")"));
            }
            SubLinkType::MULTIEXPR_SUBLINK => unimplemented!("SubLinkType::MULTIEXPR_SUBLINK"),
            SubLinkType::ARRAY_SUBLINK => {
                sql.push_str("array");
                sql.push_str(&self.subselect.sql_wrap("(", ")"));
            }
            SubLinkType::CTE_SUBLINK => unimplemented!("SubLinkType::CTE_SUBLINK"),
        }

        sql
    }
}
```

## File: `src/nodes/table_like_clause.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::Sql;
use postgres_parser::nodes::TableLikeClause;

impl Sql for TableLikeClause {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str(&self.relation.sql_prefix("LIKE "));

        sql
    }
}
```

## File: `src/nodes/transaction_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlIdent, SqlList};
use postgres_parser::nodes::TransactionStmt;
use postgres_parser::sys::TransactionStmtKind;

impl Sql for TransactionStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        match self.kind {
            TransactionStmtKind::TRANS_STMT_BEGIN | TransactionStmtKind::TRANS_STMT_START => {
                sql.push_str("BEGIN TRANSACTION ");
                sql.push_str(&self.options.sql(" "));
            }
            TransactionStmtKind::TRANS_STMT_COMMIT => {
                sql.push_str("COMMIT TRANSACTION");
                if self.chain {
                    sql.push_str(" AND CHAIN")
                }
            }
            TransactionStmtKind::TRANS_STMT_ROLLBACK => {
                sql.push_str("ROLLBACK TRANSACTION");
                if self.chain {
                    sql.push_str(" AND CHAIN")
                }
            }
            TransactionStmtKind::TRANS_STMT_SAVEPOINT => {
                sql.push_str("SAVEPOINT ");
                sql.push_str(&self.savepoint_name.sql_ident());
            }
            TransactionStmtKind::TRANS_STMT_RELEASE => {
                sql.push_str("RELEASE SAVEPOINT ");
                sql.push_str(&self.savepoint_name.sql_ident());
            }
            TransactionStmtKind::TRANS_STMT_ROLLBACK_TO => {
                sql.push_str("ROLLBACK TRANSACTION TO ");
                sql.push_str(&self.savepoint_name.sql_ident());
            }
            TransactionStmtKind::TRANS_STMT_PREPARE => {
                sql.push_str("PREPARE TRANSACTION ");
                sql.push_str(&self.gid.sql_ident());
            }
            TransactionStmtKind::TRANS_STMT_COMMIT_PREPARED => {
                sql.push_str("COMMIT PREPARED ");
                sql.push_str(&self.gid.sql_ident());
            }
            TransactionStmtKind::TRANS_STMT_ROLLBACK_PREPARED => {
                sql.push_str("ROLLBACK PREPARED ");
                sql.push_str(&self.gid.sql_ident());
            }
        }

        sql
    }
}

impl Diff for TransactionStmt {}
```

## File: `src/nodes/truncate_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlList};
use postgres_parser::nodes::TruncateStmt;

impl Sql for TruncateStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("TRUNCATE TABLE ");
        sql.push_str(&self.relations.sql(", "));
        if self.restart_seqs {
            sql.push_str("RESTART IDENTITY");
        }
        sql.push(' ');
        sql.push_str(&self.behavior.sql());
        sql
    }
}

impl Diff for TruncateStmt {}
```

## File: `src/nodes/type_cast.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::Sql;
use postgres_parser::nodes::TypeCast;

impl Sql for TypeCast {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push('(');
        sql.push('(');
        sql.push_str(
            &self
                .arg
                .as_ref()
                .expect("no 'arg' for TypeCast")
                .as_ref()
                .sql(),
        );
        sql.push(')');
        sql.push_str("::");
        sql.push_str(&self.typeName.sql());
        sql.push(')');

        sql
    }
}
```

## File: `src/nodes/type_name.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlIdent, SqlList};
use postgres_parser::nodes::TypeName;
use postgres_parser::Node;

impl Sql for TypeName {
    fn sql(&self) -> String {
        let mut sql = String::new();

        if self.setof {
            sql.push_str("SETOF ");
        }

        sql.push_str(&self.names.sql_ident());
        sql.push_str(&self.typmods.sql_wrap(",", "(", ")"));

        if let Some(array_bounds) = self.arrayBounds.as_ref() {
            for bound in array_bounds {
                if let Node::Value(bound) = bound {
                    let bound = bound.int.unwrap();
                    if bound == -1 {
                        sql.push_str("[]");
                    } else {
                        sql.push_str(&format!("[{}]", bound));
                    }
                }
            }
        }

        sql
    }
}
```

## File: `src/nodes/unlisten_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlIdent};
use postgres_parser::nodes::UnlistenStmt;

impl Sql for UnlistenStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        if self.conditionname.is_none() {
            sql.push_str("UNLISTEN *");
        } else {
            sql.push_str(&self.conditionname.sql_ident_prefix("UNLISTEN "));
        }

        sql
    }
}

impl Diff for UnlistenStmt {}
```

## File: `src/nodes/update_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::nodes::res_target::{res_target_returning, res_target_update};
use crate::schema_set::{Diff, Sql, SqlList};
use postgres_parser::nodes::UpdateStmt;

impl Sql for UpdateStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str(&self.withClause.sql());

        sql.push_str("UPDATE ");
        sql.push_str(&self.relation.sql());
        sql.push_str(" SET ");
        sql.push_str(&res_target_update(&self.targetList));

        if self.fromClause.is_some() {
            sql.push_str(" FROM ");
            sql.push_str(&self.fromClause.sql(", "));
        }

        if self.whereClause.is_some() {
            sql.push_str(" WHERE ");
            sql.push_str(&self.whereClause.sql());
        }

        sql.push_str(&res_target_returning(&self.returningList));

        sql
    }
}

impl Diff for UpdateStmt {}
```

## File: `src/nodes/vacuum_relation.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlList};
use postgres_parser::nodes::VacuumRelation;

impl Sql for VacuumRelation {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str(&self.relation.sql());
        sql.push_str(&self.va_cols.sql_wrap(", ", "(", ")"));

        sql
    }
}
```

## File: `src/nodes/vacuum_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlList};
use postgres_parser::nodes::VacuumStmt;

impl Sql for VacuumStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        if self.is_vacuumcmd {
            sql.push_str("VACUUM ");
        } else {
            sql.push_str("ANALYZE ");
        }

        sql.push_str(&self.options.sql_wrap(", ", "(", ") "));
        sql.push_str(&self.rels.sql(", "));

        sql
    }
}

impl Diff for VacuumStmt {}
```

## File: `src/nodes/value.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::Sql;
use postgres_parser::nodes::Value;

impl Sql for Value {
    fn sql(&self) -> String {
        if self.string.is_some() {
            return self.string.as_ref().unwrap().to_string();
        } else if self.int.is_some() {
            return self.int.as_ref().unwrap().to_string();
        } else if self.float.is_some() {
            return self.float.as_ref().unwrap().to_string();
        } else if self.bit_string.is_some() {
            return self.bit_string.as_ref().unwrap().to_string();
        } else if self.null.is_some() {
            return "NULL".into();
        } else {
            panic!("unexpected Value");
        }
    }
}
```

## File: `src/nodes/variable_set_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlIdent, SqlList};
use postgres_parser::nodes::VariableSetStmt;
use postgres_parser::sys::VariableSetKind;

impl Sql for VariableSetStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        match self.kind {
            VariableSetKind::VAR_SET_VALUE => {
                sql.push_str("SET ");
                if self.is_local {
                    sql.push_str("LOCAL ");
                }
                sql.push_str(&self.name.sql_ident());
                sql.push_str(" TO ");
                sql.push_str(&self.args.sql(", "));
            }
            VariableSetKind::VAR_SET_DEFAULT => {
                sql.push_str("SET ");
                if self.is_local {
                    sql.push_str("LOCAL ");
                }
                sql.push_str(&self.name.sql_ident());
                sql.push_str(" TO DEFAULT");
            }
            VariableSetKind::VAR_SET_CURRENT => {
                sql.push_str("SET ");
                if self.is_local {
                    sql.push_str("LOCAL ");
                }
                sql.push_str(&self.name.sql_ident());
                sql.push_str(" FROM CURRENT ");
            }
            VariableSetKind::VAR_SET_MULTI => unimplemented!("VariableSetKind::VAR_SET_MULTI"),
            VariableSetKind::VAR_RESET => {
                sql.push_str("RESET ");
                if self.is_local {
                    sql.push_str("LOCAL ");
                }
                sql.push_str(&self.name.sql_ident());
            }
            VariableSetKind::VAR_RESET_ALL => {
                sql.push_str("RESET ALL");
            }
        }

        sql
    }
}

impl Diff for VariableSetStmt {}
```

## File: `src/nodes/variable_show_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Sql, SqlIdent};
use postgres_parser::nodes::VariableShowStmt;

impl Sql for VariableShowStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("SHOW ");
        sql.push_str(&self.name.sql_ident());

        sql
    }
}

impl Diff for VariableShowStmt {}
```

## File: `src/nodes/vec_of_node.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlCollect, SqlList, SqlMaybeList};

use postgres_parser::Node;

fn render_node(node: &Node, sql: &mut String, sep: &str) {
    if let Node::List(node) = node {
        sql.push_str(&node.sql(sep));
    } else {
        sql.push_str(&node.sql());
    }
}

impl SqlList for Vec<Node> {
    #[track_caller]
    fn sql(&self, sep: &str) -> String {
        let mut sql = String::new();
        for (i, node) in self.iter().enumerate() {
            if i > 0 {
                sql.push_str(sep);
            }
            render_node(node, &mut sql, sep);
        }

        sql
    }

    fn sql_prefix(&self, pre: &str, sep: &str) -> String {
        format!("{}{}", pre, self.sql(sep))
    }

    fn sql_prefix_and_wrap(&self, pre: &str, start: &str, end: &str, sep: &str) -> String {
        format!("{}{}{}{}", pre, start, self.sql(sep), end)
    }

    fn sql_wrap_each(&self, pre: Option<&str>, post: Option<&str>) -> String {
        let mut sql = String::new();
        for node in self.iter() {
            if let Some(pre) = pre.as_ref() {
                sql.push_str(pre);
            }
            sql.push_str(&node.sql());
            if let Some(post) = post.as_ref() {
                sql.push_str(post);
            }
        }

        sql
    }

    fn sql_wrap_each_and_separate(&self, sep: &str, pre: &str, post: &str) -> String {
        let mut sql = String::new();
        for (i, node) in self.iter().enumerate() {
            if i > 0 {
                sql.push_str(sep);
            }

            sql.push_str(pre);
            sql.push_str(&node.sql_maybe_list(sep));
            sql.push_str(post);
        }

        sql
    }

    fn sql_wrap(&self, sep: &str, pre: &str, post: &str) -> String {
        let mut sql = String::new();
        sql.push_str(pre);
        for (i, node) in self.iter().enumerate() {
            if i > 0 {
                sql.push_str(sep);
            }

            sql.push_str(&node.sql());
        }
        sql.push_str(post);

        sql
    }
}

impl SqlList for Option<Vec<Node>> {
    fn sql(&self, sep: &str) -> String {
        match self {
            None => String::new(),
            Some(v) => v.sql(sep),
        }
    }

    fn sql_prefix(&self, pre: &str, sep: &str) -> String {
        match self {
            None => String::new(),
            Some(v) => v.sql_prefix(pre, sep),
        }
    }

    fn sql_prefix_and_wrap(&self, pre: &str, start: &str, end: &str, sep: &str) -> String {
        match self {
            None => String::new(),
            Some(v) => v.sql_prefix_and_wrap(pre, start, end, sep),
        }
    }

    fn sql_wrap_each(&self, pre: Option<&str>, post: Option<&str>) -> String {
        match self {
            None => String::new(),
            Some(v) => v.sql_wrap_each(pre, post),
        }
    }

    fn sql_wrap_each_and_separate(&self, sep: &str, pre: &str, post: &str) -> String {
        match self {
            None => String::new(),
            Some(v) => v.sql_wrap_each_and_separate(sep, pre, post),
        }
    }

    fn sql_wrap(&self, sep: &str, pre: &str, post: &str) -> String {
        match self {
            None => String::new(),
            Some(v) => v.sql_wrap(sep, pre, post),
        }
    }
}

impl<I: Iterator<Item = Node>> SqlCollect for I {
    fn sql_wrap(self, pre: &str, post: &str) -> String {
        format!("{}{}{}", pre, self.sql(), post)
    }
    fn sql(self) -> String {
        let mut sql = String::new();

        for (i, n) in self.map(|n| n.sql()).enumerate() {
            if i > 0 {
                sql.push_str(", ");
            }
            sql.push_str(&n);
        }

        sql
    }
}
```

## File: `src/nodes/view_check_option.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::Sql;
use postgres_parser::sys::ViewCheckOption;

impl Sql for ViewCheckOption {
    fn sql(&self) -> String {
        match self {
            ViewCheckOption::NO_CHECK_OPTION => "",
            ViewCheckOption::LOCAL_CHECK_OPTION => "LOCAL",
            ViewCheckOption::CASCADED_CHECK_OPTION => "CASCADED",
        }
        .into()
    }
}
```

## File: `src/nodes/view_stmt.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Diff, Len, Sql, SqlList};
use postgres_parser::nodes::ViewStmt;
use postgres_parser::Node;

impl Sql for ViewStmt {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("CREATE ");
        if self.replace {
            sql.push_str("OR REPLACE ");
        }
        sql.push_str("VIEW ");
        sql.push_str(&self.view.sql());
        if self.options.len() > 0 {
            sql.push_str(" WITH (");
            sql.push_str(&self.options.sql(", "));
            sql.push(')');
        }
        sql.push_str(" AS ");
        sql.push_str(&self.query.sql());
        sql.push(' ');
        sql.push_str(&self.withCheckOption.sql());

        sql
    }
}

impl Diff for ViewStmt {
    fn alter_stmt(&self, other: &Node) -> Option<String> {
        Some(format!("{};\n{}", self.drop_stmt().unwrap(), other.sql()))
    }

    fn drop_stmt(&self) -> Option<String> {
        Some(format!("DROP VIEW {}", self.view.sql()))
    }

    fn object_name(&self) -> Option<String> {
        Some(self.view.sql())
    }

    fn object_type(&self) -> String {
        "VIEW".into()
    }
}
```

## File: `src/nodes/window_def.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlList};
use postgres_parser::nodes::WindowDef;

impl Sql for WindowDef {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push('(');
        sql.push_str(&self.orderClause.sql_prefix("ORDER BY ", ","));
        sql.push(')');

        sql
    }
}
```

## File: `src/nodes/with_clause.rs`
```rust
// Copyright 2020-2026 Eric B. Ridge <eebbrr@gmail.com>. All rights reserved. Use
// of this source code is governed by the Postgres license that can be found in
// the LICENSE file.
use crate::schema_set::{Sql, SqlList};
use postgres_parser::nodes::WithClause;

impl Sql for WithClause {
    fn sql(&self) -> String {
        let mut sql = String::new();

        sql.push_str("WITH ");
        if self.recursive {
            sql.push_str("RECURSIVE ");
        }
        sql.push_str(&self.ctes.sql(", "));

        sql
    }
}
```

