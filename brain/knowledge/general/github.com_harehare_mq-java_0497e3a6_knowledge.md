---
id: github.com-harehare-mq-java-0497e3a6-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:05.629227
---

# KNOWLEDGE EXTRACT: github.com_harehare_mq-java_0497e3a6
> **Extracted on:** 2026-04-01 13:03:01
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007522212/github.com_harehare_mq-java_0497e3a6

---

## File: `.gitignore`
```
target/
.mq/
*.class
*.jar
*.log
.idea/
*.iml
.settings/
.project
.classpath
.DS_Store
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 harehare

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `Makefile`
```
.PHONY: setup build-rust build test clean

MQ_REPO_URL := https://github.com/harehare/mq
MQ_REPO_DIR := .mq
MQ_FFI_DIR  := $(MQ_REPO_DIR)/crates/mq-ffi
MQ_LIB_DIR  := $(MQ_REPO_DIR)/target/release

setup:
	@if [ -d "$(MQ_REPO_DIR)/.git" ]; then \
		git -C $(MQ_REPO_DIR) pull --ff-only -q; \
	else \
		git clone --depth=1 $(MQ_REPO_URL) $(MQ_REPO_DIR); \
	fi

build-rust: setup
	cd $(MQ_REPO_DIR) && cargo build --release -p mq-ffi

build: build-rust
	mvn compile -q

test: build-rust
	mvn test -Djna.library.path=$(MQ_LIB_DIR)

clean:
	mvn clean -q
```

## File: `README.md`
```markdown
<h1 align="center">mq-java</h1>

Java bindings for [mq](https://github.com/harehare/mq) — a jq-like command-line tool for Markdown processing.

## Requirements

- Java 11+
- Maven
- Rust toolchain (for building the native library)

## Setup

Clone and build the native library, then compile the Java bindings:

```bash
make build
```

Or step by step:

```bash
make setup       # Clone the mq repository
make build-rust  # Build the mq-ffi native library
mvn compile      # Compile the Java sources
```

## Running Tests

```bash
make test
```

## Usage

### Basic Query

```java
try (Mq mq = new Mq()) {
    MqResult result = mq.run(".h1", "# Hello World\n\nSome text");
    System.out.println(result.text()); // "# Hello World"
}
```

### Input Formats

```java
try (Mq mq = new Mq()) {
    // Markdown (default)
    MqResult md = mq.run(".h2", content, InputFormat.MARKDOWN);

    // MDX
    MqResult mdx = mq.run("select(is_mdx())", content, InputFormat.MDX);

    // HTML (auto-converted to Markdown)
    MqResult html = mq.run(".h1", "<h1>Title</h1>", InputFormat.HTML);

    // Plain text (split by lines)
    MqResult text = mq.run("select(contains(\"foo\"))", content, InputFormat.TEXT);
}
```

### HTML to Markdown Conversion

```java
String markdown = Mq.htmlToMarkdown("<h1>Hello</h1><p>World</p>");
```

With options:

```java
ConversionOptions options = new ConversionOptions();
options.useTitleAsH1 = true;
options.generateFrontMatter = true;
options.extractScriptsAsCodeBlocks = true;

String markdown = Mq.htmlToMarkdown(html, options);
```

### Working with Results

```java
MqResult result = mq.run(".h2", content);

// Get all values joined by newline
String text = result.text();

// Get as a list
List<String> values = result.values();

// Access by index
String first = result.get(0);

// Iterate
for (String value : result) {
    System.out.println(value);
}
```

## API

### `Mq`

| Method | Description |
|---|---|
| `run(String code, String content)` | Run a query on Markdown content |
| `run(String code, String content, InputFormat format)` | Run a query with a specified input format |
| `static htmlToMarkdown(String html)` | Convert HTML to Markdown |
| `static htmlToMarkdown(String html, ConversionOptions options)` | Convert HTML to Markdown with options |
| `close()` | Release native resources (`AutoCloseable`) |

### `InputFormat`

| Value | Description |
|---|---|
| `MARKDOWN` | CommonMark / GFM (default) |
| `MDX` | Markdown with JSX |
| `HTML` | HTML (auto-converted to Markdown) |
| `TEXT` | Plain text, split by lines |
| `RAW` | Raw input, no parsing |

### `ConversionOptions`

| Field | Type | Description |
|---|---|---|
| `extractScriptsAsCodeBlocks` | `boolean` | Extract `<script>` tags as code blocks |
| `generateFrontMatter` | `boolean` | Generate front matter from HTML `<head>` metadata |
| `useTitleAsH1` | `boolean` | Use `<title>` as an H1 heading |

## License

[MIT](LICENSE)
```

## File: `pom.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.github.harehare</groupId>
    <artifactId>mq-java</artifactId>
    <version>0.1.0</version>
    <packaging>jar</packaging>

    <name>mq-java</name>
    <description>Java bindings for mq - a jq-like command-line tool for Markdown processing</description>
    <url>https://github.com/harehare/mq-java</url>

    <licenses>
        <license>
            <name>MIT License</name>
            <url>https://opensource.org/licenses/MIT</url>
        </license>
    </licenses>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <jna.version>5.14.0</jna.version>
        <junit.version>5.10.2</junit.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>net.java.dev.jna</groupId>
            <artifactId>jna</artifactId>
            <version>${jna.version}</version>
        </dependency>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>${junit.version}</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.2.5</version>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.12.1</version>
                <configuration>
                    <source>11</source>
                    <target>11</target>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

## File: `src/main/java/com/github/harehare/mq/ConversionOptions.java`
```java
package com.github.harehare.mq;

import com.sun.jna.Structure;

import java.util.Arrays;
import java.util.List;

/**
 * Options for HTML to Markdown conversion.
 *
 * <p>This class maps directly to the {@code MqConversionOptions} C struct
 * used by the mq-ffi library.</p>
 */
public class ConversionOptions extends Structure {

    /** Extract script tags as code blocks. */
    public boolean extractScriptsAsCodeBlocks;

    /** Generate front matter from HTML head metadata. */
    public boolean generateFrontMatter;

    /** Use HTML title tag as H1 heading. */
    public boolean useTitleAsH1;

    /**
     * Creates a new ConversionOptions with all options set to false.
     */
    public ConversionOptions() {
        this.extractScriptsAsCodeBlocks = false;
        this.generateFrontMatter = false;
        this.useTitleAsH1 = false;
    }

    @Override
    protected List<String> getFieldOrder() {
        return Arrays.asList(
                "extractScriptsAsCodeBlocks",
                "generateFrontMatter",
                "useTitleAsH1"
        );
    }
}
```

## File: `src/main/java/com/github/harehare/mq/InputFormat.java`
```java
package com.github.harehare.mq;

/**
 * Input format for mq query processing.
 */
public enum InputFormat {
    /** Standard Markdown (CommonMark/GFM) */
    MARKDOWN("markdown"),
    /** Markdown with JSX support */
    MDX("mdx"),
    /** Plain text (split by lines) */
    TEXT("text"),
    /** HTML content (auto-converted to Markdown) */
    HTML("html"),
    /** Raw input format (no parsing, returns original content) */
    RAW("RAW");

    private final String value;

    InputFormat(String value) {
        this.value = value;
    }

    /**
     * Returns the string value used by the FFI layer.
     *
     * @return the format string
     */
    public String getValue() {
        return value;
    }
}
```

## File: `src/main/java/com/github/harehare/mq/Mq.java`
```java
package com.github.harehare.mq;

import com.sun.jna.Pointer;
import com.sun.jna.ptr.PointerByReference;

/**
 * Java bindings for mq - a jq-like tool for Markdown processing.
 *
 * <p>This class wraps the mq-ffi native library, providing a safe, idiomatic Java API
 * for querying and transforming Markdown, MDX, HTML, and text content.</p>
 *
 * <p>Example usage:</p>
 * <pre>{@code
 * try (Mq mq = new Mq()) {
 *     MqResult result = mq.run(".h1", "# Hello World\n\nText");
 *     System.out.println(result.text()); // "# Hello World"
 * }
 * }</pre>
 */
public class Mq implements AutoCloseable {

    private Pointer engine;

    /**
     * Creates a new mq engine instance.
     *
     * @throws MqException if the engine could not be created
     */
    public Mq() {
        this.engine = MqLibrary.INSTANCE.mq_create();
        if (this.engine == null) {
            throw new MqException("Failed to create mq engine");
        }
    }

    /**
     * Executes an mq query on the provided content using Markdown format.
     *
     * @param code    the mq query string
     * @param content the content to process
     * @return the query result
     * @throws MqException if the query fails
     */
    public MqResult run(String code, String content) {
        return run(code, content, InputFormat.MARKDOWN);
    }

    /**
     * Executes an mq query on the provided content.
     *
     * @param code        the mq query string
     * @param content     the content to process
     * @param inputFormat the input format
     * @return the query result
     * @throws MqException if the query fails
     */
    public MqResult run(String code, String content, InputFormat inputFormat) {
        ensureOpen();
        MqLibrary.MqResultStruct.ByValue result = MqLibrary.INSTANCE.mq_eval(
                engine, code, content, inputFormat.getValue()
        );
        try {
            if (result.errorMsg != null && result.errorMsg != Pointer.NULL) {
                String error = result.errorMsg.getString(0);
                throw new MqException(error);
            }
            String[] values = new String[(int) result.valuesLen];
            if (result.values != null && result.valuesLen > 0) {
                Pointer[] pointers = result.values.getPointerArray(0, (int) result.valuesLen);
                for (int i = 0; i < pointers.length; i++) {
                    values[i] = pointers[i] != null ? pointers[i].getString(0) : "";
                }
            }
            return new MqResult(values);
        } finally {
            MqLibrary.INSTANCE.mq_free_result(result);
        }
    }

    /**
     * Converts HTML content to Markdown.
     *
     * @param htmlContent the HTML content to convert
     * @return the converted Markdown string
     * @throws MqException if the conversion fails
     */
    public static String htmlToMarkdown(String htmlContent) {
        return htmlToMarkdown(htmlContent, new ConversionOptions());
    }

    /**
     * Converts HTML content to Markdown with the specified options.
     *
     * @param htmlContent the HTML content to convert
     * @param options     the conversion options
     * @return the converted Markdown string
     * @throws MqException if the conversion fails
     */
    public static String htmlToMarkdown(String htmlContent, ConversionOptions options) {
        PointerByReference errorMsgRef = new PointerByReference();
        Pointer resultPtr = MqLibrary.INSTANCE.mq_html_to_markdown(
                htmlContent, options, errorMsgRef
        );
        if (resultPtr == null || resultPtr == Pointer.NULL) {
            Pointer errorPtr = errorMsgRef.getValue();
            String error = errorPtr != null ? errorPtr.getString(0) : "Unknown error";
            if (errorPtr != null) {
                MqLibrary.INSTANCE.mq_free_string(errorPtr);
            }
            throw new MqException(error);
        }
        try {
            return resultPtr.getString(0);
        } finally {
            MqLibrary.INSTANCE.mq_free_string(resultPtr);
        }
    }

    /**
     * Closes the mq engine and releases native resources.
     */
    @Override
    public void close() {
        if (engine != null) {
            MqLibrary.INSTANCE.mq_destroy(engine);
            engine = null;
        }
    }

    private void ensureOpen() {
        if (engine == null) {
            throw new MqException("Mq engine has been closed");
        }
    }
}
```

## File: `src/main/java/com/github/harehare/mq/MqException.java`
```java
package com.github.harehare.mq;

/**
 * Exception thrown when an mq operation fails.
 */
public class MqException extends RuntimeException {

    /**
     * Creates a new MqException with the specified message.
     *
     * @param message the error message
     */
    public MqException(String message) {
        super(message);
    }
}
```

## File: `src/main/java/com/github/harehare/mq/MqLibrary.java`
```java
package com.github.harehare.mq;

import com.sun.jna.Library;
import com.sun.jna.Native;
import com.sun.jna.Pointer;
import com.sun.jna.Structure;
import com.sun.jna.ptr.PointerByReference;

import java.util.Arrays;
import java.util.List;

/**
 * JNA interface to the mq-ffi native library.
 */
interface MqLibrary extends Library {

    MqLibrary INSTANCE = Native.load("mq_ffi", MqLibrary.class);

    /**
     * C-compatible result structure.
     */
    class MqResultStruct extends Structure {
        public Pointer values;
        public long valuesLen;
        public Pointer errorMsg;

        public MqResultStruct() {
            super();
        }

        @Override
        protected List<String> getFieldOrder() {
            return Arrays.asList("values", "valuesLen", "errorMsg");
        }

        public static class ByValue extends MqResultStruct implements Structure.ByValue {
        }
    }

    Pointer mq_create();

    void mq_destroy(Pointer enginePtr);

    MqResultStruct.ByValue mq_eval(Pointer enginePtr, String code, String input, String inputFormat);

    void mq_free_result(MqResultStruct.ByValue result);

    Pointer mq_html_to_markdown(String htmlInput, ConversionOptions options, PointerByReference errorMsg);

    void mq_free_string(Pointer s);
}
```

## File: `src/main/java/com/github/harehare/mq/MqResult.java`
```java
package com.github.harehare.mq;

import java.util.Arrays;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;
import java.util.stream.Collectors;

/**
 * Result of an mq query evaluation.
 *
 * <p>Contains the list of string values produced by the query.</p>
 */
public class MqResult implements Iterable<String> {

    private final List<String> values;

    MqResult(String[] values) {
        this.values = values != null
                ? Collections.unmodifiableList(Arrays.asList(values))
                : Collections.emptyList();
    }

    /**
     * Returns all result values joined by newlines.
     *
     * @return the text representation
     */
    public String text() {
        return values.stream()
                .filter(v -> v != null && !v.isEmpty())
                .collect(Collectors.joining("\n"));
    }

    /**
     * Returns all non-empty result values as a list.
     *
     * @return the list of values
     */
    public List<String> values() {
        return values.stream()
                .filter(v -> v != null && !v.isEmpty())
                .collect(Collectors.toList());
    }

    /**
     * Returns the total number of result values.
     *
     * @return the count
     */
    public int length() {
        return values.size();
    }

    /**
     * Returns the value at the specified index.
     *
     * @param index the zero-based index
     * @return the value at the index
     * @throws IndexOutOfBoundsException if the index is out of range
     */
    public String get(int index) {
        return values.get(index);
    }

    @Override
    public Iterator<String> iterator() {
        return values.iterator();
    }
}
```

## File: `src/test/java/com/github/harehare/mq/MqTest.java`
```java
package com.github.harehare.mq;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class MqTest {

    private Mq mq;

    @BeforeEach
    void setUp() {
        mq = new Mq();
    }

    @AfterEach
    void tearDown() {
        mq.close();
    }

    @Nested
    class Run {

        @Test
        void extractsH1Headings() {
            String content = "# Hello World\n\n## Heading2\n\nText";
            MqResult result = mq.run(".h1", content);
            assertEquals(List.of("# Hello World"), result.values());
        }

        @Test
        void extractsH2Headings() {
            String content = "# Hello World\n\n## Heading2\n\nText";
            MqResult result = mq.run(".h2", content);
            assertEquals(List.of("## Heading2"), result.values());
        }

        @Test
        void extractsMultipleH2Headings() {
            String content = "# Main Title\n\n## Heading2A\n\nText\n\n## Heading2B\n\nMore text";
            MqResult result = mq.run(".h2", content);
            assertEquals(List.of("## Heading2A", "## Heading2B"), result.values());
        }

        @Test
        void filtersHeadingsWithSelect() {
            String content = "# Product\n\n## Features\n\nText\n\n## Installation\n\nMore text";
            MqResult result = mq.run(".h2 | select(contains(\"Feature\"))", content);
            assertEquals(List.of("## Features"), result.values());
        }

        @Test
        void extractsListItems() {
            String content = "# List\n\n- Item 1\n- Item 2\n- Item 3";
            MqResult result = mq.run(".[]", content);
            assertEquals(List.of("- Item 1", "- Item 2", "- Item 3"), result.values());
        }

        @Test
        void extractsCodeBlocks() {
            String content = "# Code\n\n```python\nprint('Hello')\n```";
            MqResult result = mq.run(".code", content);
            assertEquals(List.of("```python\nprint('Hello')\n```"), result.values());
        }
    }

    @Nested
    class InputFormats {

        @Test
        void processesTextFormat() {
            String content = "Line 1\nLine 2\nLine 3";
            MqResult result = mq.run("select(contains(\"2\"))", content, InputFormat.TEXT);
            assertEquals(List.of("Line 2"), result.values());
        }

        @Test
        void processesMdxFormat() {
            String content = "# MDX Content\n\n<Component />";
            MqResult result = mq.run("select(is_mdx())", content, InputFormat.MDX);
            assertEquals(List.of("<Component />"), result.values());
        }

        @Test
        void processesHtmlFormat() {
            String content = "<h1>Hello</h1><p>World</p>";
            MqResult result = mq.run("select(contains(\"Hello\"))", content, InputFormat.HTML);
            assertEquals(List.of("# Hello"), result.values());
        }
    }

    @Nested
    class ErrorHandling {

        @Test
        void throwsExceptionForInvalidSyntax() {
            assertThrows(MqException.class, () -> {
                mq.run(".invalid_selector!!!", "# Heading");
            });
        }

        @Test
        void throwsExceptionWhenClosed() {
            mq.close();
            assertThrows(MqException.class, () -> {
                mq.run(".h1", "# Heading");
            });
        }
    }

    @Nested
    class HtmlToMarkdown {

        @Test
        void convertsHtmlToMarkdown() {
            String html = "<h1>Hello World</h1><p>This is a <strong>test</strong>.</p>";
            String markdown = Mq.htmlToMarkdown(html);
            assertTrue(markdown.contains("# Hello World"));
            assertTrue(markdown.contains("**test**"));
        }

        @Test
        void convertsHtmlWithOptions() {
            String html = "<html><head><title>Page Title</title></head><body><h1>Content</h1></body></html>";
            ConversionOptions options = new ConversionOptions();
            options.useTitleAsH1 = true;
            String markdown = Mq.htmlToMarkdown(html, options);
            assertTrue(markdown.contains("# Page Title"));
        }
    }

    @Nested
    class MqResultTest {

        @Test
        void textJoinsValues() {
            String content = "# Title\n\n## Section 1\n\n## Section 2";
            MqResult result = mq.run(".h2", content);
            assertEquals("## Section 1\n## Section 2", result.text());
        }

        @Test
        void valuesReturnsNonEmptyValues() {
            String content = "# Title\n\n## Section 1\n\n## Section 2";
            MqResult result = mq.run(".h2", content);
            assertEquals(List.of("## Section 1", "## Section 2"), result.values());
        }

        @Test
        void lengthReturnsCount() {
            String content = "# Title\n\n## Section 1\n\n## Section 2";
            MqResult result = mq.run(".h2", content);
            assertTrue(result.length() > 0);
        }

        @Test
        void getAccessesByIndex() {
            String content = "# Title\n\n## Section 1\n\n## Section 2";
            MqResult result = mq.run(".h2", content);
            List<String> values = result.values();
            assertEquals("## Section 1", values.get(0));
            assertEquals("## Section 2", values.get(1));
        }

        @Test
        void iteratorWorks() {
            String content = "# Title\n\n## Section 1\n\n## Section 2";
            MqResult result = mq.run(".h2", content);
            List<String> collected = new ArrayList<>();
            for (String value : result) {
                collected.add(value);
            }
            assertTrue(collected.size() > 0);
        }
    }
}
```

