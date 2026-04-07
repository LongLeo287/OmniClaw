---
id: hexhog
type: knowledge
owner: OA_Triage
---
# hexhog
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# hexhog

A configurable hex viewer/editor

![hexhog lol](hexhog.gif)

To run `hexhog`, use the following command:
```
hexhog <file>
```

## Installation
If you have cargo installed, you can run the following command:
```
cargo install hexhog
```

It is also available on AUR and Homebrew, thanks to [@dhopcs](https://github.com/dhopcs) and [@chenrui333](https://github.com/chenrui333).
```
yay -S hexhog
```

```
brew install hexhog
```

I hope to make this tool available on other package managers soon.

## Features
For now, `hexhog` allows for basic hex editing features for files, such as editing/deleting/inserting bytes, as well as selecting and copy/pasting bytes. I'm look forward to adding other features, including (but not only):
- moving the selection
- find/replace
- bookmarks
- better navigation
- CP437
- other coloring options

While I do love (and use) modal editors, `hexhog` does not attempt to be one. I am trying to make it as intuitive as possible :)

## Configuration

You can find the configuration file in the following locations:
- Linux: `/home/user/.config/hexhog/config.toml`
- Windows: `C:\Users\user\AppData\Roaming\hexhog\config.toml`
- MacOS: `/Users/user/Library/Application Support/hexhog/config.toml`

An example configuration file:
```toml
[theme]
null = "dark_gray"
ascii_printable = "blue"
ascii_whitespace = [67, 205, 128] # rgb
ascii_other = 162 # ansi
non_ascii = "red"
accent = "blue"
primary = "green"
background = "black"
border = "cyan"

[charset]
null = "."
ascii_whitespace = "·"
ascii_other = "°"
non_ascii = "×"
```

## Feedback

Feedback on `hexhog` is highly appreciated. Thanks! :D

## License

Copyright &copy; dvdtsb 2025

This project uses the MIT license ([LICENSE] or [http://opensource.org/licenses/MIT](http://opensource.org/licenses/MIT)).

[LICENSE]: ./LICENSE

```

### File: CHANGELOG.md
```md
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.3](https://github.com/DVDTSB/hexhog/compare/v0.1.2...v0.1.3) - 2025-11-06

### Fixed

- fix fmt
- fix fmt
- fix fmt!
- fix fmt
- fix unexistent file thing
- fix clippy
- fixed workflow
- fixed gif
- fix clippy

### Other

- gif
- organize render
- remove state from status
- organize stuff, fix backspace
- add temp gif
- stuff lol
- colors!
- update help
- rework changes (should probably rename to actions), add copy pasting
- exit selection
- selection ish
- selection start, make stuff that should be usize  usize
- merge insert and edit modes. also fix insert offset thing
- add delete, fix newline thing
- added pageup/pagedown key support for page-wise navigation
- release v0.1.2
- added writing to back of file and refactored a bit of drawing logic
- meow
- add insert mode
- release v0.1.1
- finished config
- change options to results
- structure+basic config
- Add GitHub Actions workflow for releases
- meow
- add gif
- basic functionality
- added editing, saving, undo and help
- meow
- init
- init

## [0.1.2](https://github.com/DVDTSB/hexhog/compare/v0.1.1...v0.1.2) - 2025-10-09

### Fixed

- fix unexistent file thing
- fix clippy

### Other

- added writing to back of file and refactored a bit of drawing logic
- meow
- add insert mode

## [0.1.1](https://github.com/DVDTSB/hexhog/compare/v0.1.0...v0.1.1) - 2025-09-27

### Other

- change options to results
- structure+basic config
- Add GitHub Actions workflow for releases

```

### File: src\byte.rs
```rs
use ratatui::style::Style;

use crate::config::Config;

#[derive(Clone, Copy, PartialEq, Eq)]
pub struct Byte(u8);

pub enum ByteType {
    Null,
    AsciiPrintable,
    AsciiWhitespace,
    AsciiOther,
    NonAscii,
}

impl Byte {
    pub fn new(value: u8) -> Self {
        Byte(value)
    }

    pub fn value(&self) -> u8 {
        self.0
    }

    pub fn get_bytetype(self) -> ByteType {
        match self.0 {
            0 => ByteType::Null,
            c if c.is_ascii_graphic() => ByteType::AsciiPrintable,
            c if c.is_ascii_whitespace() => ByteType::AsciiWhitespace,
            c if c.is_ascii() => ByteType::AsciiOther,
            _ => ByteType::NonAscii,
        }
    }

    pub fn get_hex(self) -> String {
        format!("{:02X}", self.0)
    }

    pub fn get_char(self, config: &Config) -> char {
        config.charset.get_char(&self)
    }

    pub fn get_style(&self, config: &Config) -> Style {
        config.colorscheme.get_style(self)
    }
}

```

### File: src\config.rs
```rs
use std::{fs::read_to_string, str::FromStr};

use crate::byte::{Byte, ByteType};
use ratatui::style::{Color, Style};
use toml::Table;

pub struct ColorScheme {
    pub null: Color,
    pub ascii_printable: Color,
    pub ascii_whitespace: Color,
    pub ascii_other: Color,
    pub non_ascii: Color,
    pub accent: Color,
    pub primary: Color,
    pub border: Color,
    pub select: Color,
    pub background: Color,
}

impl ColorScheme {
    pub fn get_style(&self, byte: &Byte) -> Style {
        match byte.get_bytetype() {
            ByteType::Null => Style::default().fg(self.null),
            ByteType::AsciiPrintable => Style::default().fg(self.ascii_printable),
            ByteType::AsciiWhitespace => Style::default().fg(self.ascii_whitespace),
            ByteType::AsciiOther => Style::default().fg(self.ascii_other),
            ByteType::NonAscii => Style::default().fg(self.non_ascii),
        }
    }
}

pub struct Charset {
    pub null: char,
    pub ascii_whitespace: char,
    pub ascii_other: char,
    pub non_ascii: char,
}

impl Charset {
    pub fn get_char(&self, byte: &Byte) -> char {
        match byte.get_bytetype() {
            ByteType::Null => self.null,
            ByteType::AsciiPrintable => byte.value() as char,
            ByteType::AsciiWhitespace if byte.value() as char == ' ' => ' ',
            ByteType::AsciiWhitespace => self.ascii_whitespace,
            ByteType::AsciiOther => self.ascii_other,
            ByteType::NonAscii => self.non_ascii,
        }
    }
}

pub struct Config {
    pub colorscheme: ColorScheme,
    pub charset: Charset,
}

impl Default for Config {
    fn default() -> Self {
        Config {
            colorscheme: ColorScheme {
                null: Color::DarkGray,
                ascii_printable: Color::Blue,
                ascii_whitespace: Color::Cyan,
                ascii_other: Color::Yellow,
                non_ascii: Color::Green,
                accent: Color::Blue,
                select: Color::DarkGray,
                border: Color::White,
                primary: Color::White,
                background: Color::Reset,
            },
            charset: Charset {
                null: '.',
                ascii_whitespace: '·',
                ascii_other: '°',
                non_ascii: '×',
            },
        }
    }
}

impl Config {
    pub fn toml_value_to_color(value: &toml::Value) -> Result<Color, String> {
        if let Some(s) = value.as_str() {
            Color::from_str(s).map_err(|_| "Invalid color name".into())
        } else if let Some(i) = value.as_integer() {
            if (0..=255).contains(&i) {
                Ok(Color::Indexed(i as u8))
            } else {
                Err("Invalid color index".into())
            }
        } else if let Some((r, g, b)) = value.as_array().and_then(|arr| {
            if arr.len() == 3 {
                let r = arr[0].as_integer()?;
                let g = arr[1].as_integer()?;
                let b = arr[2].as_integer()?;
                if (0..=255).contains(&r) && (0..=255).contains(&g) && (0..=255).contains(&b) {
                    Some((r as u8, g as u8, b as u8))
                } else {
                    None
                }
            } else {
                None
            }
        }) {
            Ok(Color::Rgb(r, g, b))
        } else {
            Err("Invalid color format".into())
        }
    }

    fn set_color_field(table: &Table, field: &str, current: &mut Color) -> Result<(), String> {
        if let Some(value) = table.get(field) {
            let color = Config::toml_value_to_color(value);
            if color.is_err() {
                return Err(format!(
                    "Invalid color for field '{}' - {}",
                    field,
                    color.err().unwrap()
                ));
            } else {
                *current = color.unwrap()
            }
        }
        Ok(())
    }

    fn set_charset_field(table: &Table, field: &str, current: &mut char) -> Result<(), String> {
        if let Some(value) = table.get(field) {
            if let Some(s) = value.as_str() {
                let mut chars = s.chars();
                if let Some(c) = chars.next() {
                    if chars.next().is_none() {
                        *current = c;
                    } else {
                        return Err(format!("Field '{field}' must be a single character"));
                    }
                } else {
                    return Err(format!("Field '{field}' cannot be empty"));
                }
            } else {
                return Err(format!("Field '{field}' must be a string"));
            }
        }
        Ok(())
    }

    pub fn read_config(path: &str) -> Result<Self, String> {
        let mut config = Config::default();

        let config_file = read_to_string(path);

        if config_file.is_err() {
            return Ok(config);
        }

        let values = config_file.unwrap().parse::<Table>().unwrap();

        if let Some(colors) = values.get("theme") {
            if let Some(table) = colors.as_table() {
                Config::set_color_field(table, "null", &mut config.colorscheme.null)?;
                Config::set_color_field(
                    table,
                    "ascii_printable",
                    &mut config.colorscheme.ascii_printable,
                )?;
                Config::set_color_field(
                    table,
                    "ascii_whitespace",
                    &mut config.colorscheme.ascii_whitespace,
                )?;
                Config::set_color_field(table, "ascii_other", &mut config.colorscheme.ascii_other)?;
                Config::set_color_field(table, "non_ascii", &mut config.colorscheme.non_ascii)?;
                Config::set_color_field(table, "accent", &mut config.colorscheme.accent)?;
                Config::set_color_field(table, "select", &mut config.colorscheme.select)?;
                Config::set_color_field(table, "primary", &mut config.colorscheme.primary)?;
                Config::set_color_field(table, "border", &mut config.colorscheme.border)?;
                Config::set_color_field(table, "background", &mut config.colorscheme.background)?;
            }
        }

        if let Some(charset) = values.get("charset") {
            if let Some(table) = charset.as_table() {
                Config::set_charset_field(table, "null", &mut config.charset.null)?;
                Config::set_charset_field(
                    table,
                    "ascii_whitespace",
                    &mut config.charset.ascii_whitespace,
                )?;
                Config::set_charset_field(table, "ascii_other", &mut config.charset.ascii_other)?;
                Config::set_charset_field(table, "non_ascii", &mut config.charset.non_ascii)?;
                Config::set_charset_field(table, "non_ascii", &mut config.charset.non_ascii)?;
            }
        }

        Ok(config)
    }
}

```

### File: src\main.rs
```rs
mod app;
mod byte;
mod config;

use app::{App, Args};
use clap::Parser;
use color_eyre::Result;
use config::Config;

fn main() -> Result<()> {
    color_eyre::install()?;
    let args = Args::parse();

    let config_file_path = dirs::config_dir()
        .unwrap()
        .join("hexhog")
        .join("config.toml");

    let config = Config::read_config(config_file_path.to_str().unwrap()).unwrap_or_else(|e| {
        eprintln!("Error reading config: {e}");
        eprintln!("Using default config");
        Config::default()
    });

    let app = App::new(args, config)?;
    let terminal = ratatui::init();
    let result = app.run(terminal);
    ratatui::restore();
    result
}

```

### File: src\app\change.rs
```rs
use crate::app::App;

#[derive(Debug, Clone)]
pub enum Change {
    Edit(usize, Vec<u8>, Vec<u8>),
    Insert(usize, Vec<u8>),
    Delete(usize, Vec<u8>),
}

impl App {
    pub fn do_change(&mut self, change: Change) {
        self.changes.push(change.clone());
        match change {
            Change::Edit(idx, _old, new) => self.replace_data(idx, new),
            Change::Insert(idx, new) => self.insert_data(idx, new),
            Change::Delete(idx, old) => self.delete_data(idx, old.len()),
        }
    }

    pub fn undo_change(&mut self, change: Change) {
        self.made_changes.push(change.clone());
        match change {
            Change::Edit(idx, old, _new) => self.replace_data(idx, old),
            Change::Insert(idx, new) => self.delete_data(idx, new.len()),
            Change::Delete(idx, old) => self.insert_data(idx, old),
        }
    }

    pub fn undo(&mut self) {
        if let Some(change) = self.changes.pop() {
            self.undo_change(change);
        }
    }

    pub fn redo(&mut self) {
        if let Some(change) = self.made_changes.pop() {
            self.do_change(change);
        }
    }
}

```

### File: src\app\events.rs
```rs
use crate::app::{App, change::Change, state::AppState};
use color_eyre::eyre::Result;
use crossterm::event::{self, Event, KeyCode, KeyEvent, KeyEventKind, KeyModifiers};
impl App {
    pub fn handle_crossterm_events(&mut self) -> Result<()> {
        match event::read()? {
            Event::Key(key) if key.kind == KeyEventKind::Press => self.on_key_event(key),
            _ => {}
        }
        Ok(())
    }

    fn on_key_event(&mut self, key: KeyEvent) {
        match self.state {
            AppState::Move => match (key.modifiers, key.code) {
                (_, KeyCode::Char('q')) => self.quit(),
                (_, KeyCode::Right) => self.move_right(),
                (_, KeyCode::Left) => self.move_left(),
                (_, KeyCode::Up) => self.move_up(),
                (_, KeyCode::Down) => self.move_down(),
                (_, KeyCode::PageUp) => self.move_page_up(),
                (_, KeyCode::PageDown) => self.move_page_down(),

                (_, KeyCode::Char('v')) => {
                    if self.is_selecting {
                        self.is_selecting = false;
                    } else {
                        self.is_selecting = true;
                        self.selection_start = self.get_idx();
                    }
                }

                (_, KeyCode::Esc) => {
                    self.is_selecting = false;
                }

                (_, KeyCode::Char('y')) => {
                    self.clipboard = self.get_selection_data();
                    self.is_selecting = false;
                }
                (_, KeyCode::Char('p')) => {
                    self.do_change(Change::Insert(self.get_idx(), self.clipboard.clone()));
                    self.selection_start = self.get_idx();
                    self.is_selecting = true;
                    self.set_idx(self.selection_start + self.clipboard.len() - 1);
                }

                (_, KeyCode::Backspace) => {
                    let idx = self.get_idx();
                    let (x, y) = self.selection_range();

                    //since cursor can also be outside data check this lol;
                    if x == y && y == self.data.len() {
                        self.move_left();
                        return ();
                    }

                    let old = self.data[x..(y + 1)].to_vec();

                    self.do_change(Change::Delete(idx, old));

                    //if where the cursor was now theres nothing then move it!
                    let new_idx = idx.min(self.data.len().saturating_sub(1));
                    self.set_idx(new_idx);
                }
                (KeyModifiers::NONE, KeyCode::Char(c)) if c.is_ascii_hexdigit() => {
                    self.is_selecting = false;
                    self.state = AppState::Edit;
                    self.is_inserting = false;
                    self.insert_to_buffer(c);
                }

                /*
                //i really wanna do this but for some reason it doesnt work with numbers
                // for later!
                (KeyModifiers::SHIFT, KeyCode::Char(c)) if c.is_ascii_hexdigit() => {
                    self.state = AppState::Edit;
                    self.is_inserting = true;
                    self.insert_to_buffer(c);
                },
                */
                (_, KeyCode::Char('i')) => {
                    self.is_selecting = false;
                    self.state = AppState::Edit;
                    self.is_inserting = true;
                }

                (KeyModifiers::NONE, KeyCode::Char('u'))
                | (KeyModifiers::NONE, KeyCode::Char('U')) => {
                    self.is_selecting = false;
                    self.undo();
                }
                (KeyModifiers::SHIFT, KeyCode::Char('u'))
                | (KeyModifiers::SHIFT, KeyCode::Char('U')) => {
                    self.is_selecting = false;
                    self.redo();
                }
                (_, KeyCode::Char('s')) | (_, KeyCode::Char('S')) => self.save(),
                (_, KeyCode::Char('h')) | (_, KeyCode::Char('H')) => {
                    self.is_selecting = false;
                    self.state = AppState::Help;
                }

                _ => {}
            },
            AppState::Edit => match (key.modifiers, key.code) {
                (_, KeyCode::Esc) | (_, KeyCode::Backspace) => {
                    self.state = AppState::Move;
                    self.buffer = [' ', ' '];
                }
                (_, KeyCode::Char(c)) if c.is_ascii_hexdigit() => {
                    self.insert_to_buffer(c);
                    if self.buffer[0] != ' ' && self.buffer[1] != ' ' {
                        self.state = AppState::Move;
                        let idx = self.get_idx();
                        let new = self.buffer_to_u8();

                        if self.is_inserting {
                            self.do_change(Change::Insert(idx, vec![new]));
                        } else {
                            if idx >= self.data.len() {
                                self.data.push(new);
                            } else {
                                let old = self.data[idx];
                                self.do_change(Change::Edit(idx, vec![old], vec![new]))
                            }
                        }
                        self.buffer = [' ', ' '];
                        self.move_right();
                        self.is_inserting = false;
                    }
                }
                _ => {}
            },
            AppState::Help => {
                self.state = AppState::Move;
            }
        }
    }
}

```

### File: src\app\mod.rs
```rs
mod change;
mod events;
mod render;
mod state;
mod utils;
pub use state::{App, Args};

```

### File: src\app\render.rs
```rs
use crate::app::{App, state::AppState};
use ratatui::{
    Frame,
    layout::{Constraint, Direction, Flex, Layout, Rect},
    prelude::Alignment,
    style::{Style, Styled, Stylize},
    text::{Line, Span, Text},
    widgets::{Block, Borders, Clear, Padding, Paragraph},
};

use crate::byte::Byte;

impl App {
    pub fn render(&mut self, frame: &mut Frame) {
        self.render_background(frame);

        let layout = Layout::default()
            .direction(Direction::Vertical)
            .constraints([
                Constraint::Length(1),
                Constraint::Min(5),
                Constraint::Length(1),
            ])
            .split(frame.area());

        self.frame_height = layout[1].height as usize;

        self.render_title(frame, layout[0]);
        self.render_status(frame, layout[2]);
        self.render_editor(frame, layout[1]);

        if self.state == AppState::Help {
            self.render_help_popup(frame, layout[1]);
        }
    }

    fn render_background(&self, frame: &mut Frame) {
        let area = frame.area();
        let buffer = frame.buffer_mut();

        buffer.set_style(
            area,
            Style::default().bg(self.config.colorscheme.background),
        );
    }

    fn render_title(&self, frame: &mut Frame, area: Rect) {
        let title = Paragraph::new(format!(" hexhog ─ {} ", self.file_name))
            .alignment(Alignment::Center)
            .fg(self.config.colorscheme.accent);
        frame.render_widget(title, area);
    }

    fn render_status(&self, frame: &mut Frame, area: Rect) {
        let used_area = Layout::default()
            .direction(Direction::Horizontal)
            .constraints([Constraint::Length(8 + 48 + 2 + 2 + 16)])
            .flex(Flex::Center)
            .split(area);

        let status_text = format!(
            " h - help │ cursor: {:08X} │ size: {} bytes ",
            self.get_idx(),
            self.data.len(),
        );
        let status = Paragraph::new(status_text)
            .alignment(Alignment::Center)
            .fg(self.config.colorscheme.accent)
            .reversed();
        frame.render_widget(status, used_area[0]);
    }

    fn render_editor(&self, frame: &mut Frame, area: Rect) {
        let columns = Layout::default()
            .direction(Direction::Horizontal)
            .constraints([
                Constraint::Length(8),
                Constraint::Length(48 + 2 + 2),
                Constraint::Length(16),
            ])
            .flex(Flex::Center)
            .split(area);

        let mut addr_text = Text::default();
        let mut hex_text = Text::default();
        let mut ascii_text = Text::default();

        let mut offset = 0;

        for i in self.starting_line..self.starting_line + area.height as usize {
            let row_start = i * 16;

            if row_start > self.data.len() {
                break;
            }

            let addr_style = if i == self.cursor_y {
                Style::default().fg(self.config.colorscheme.primary)
            } else {
                Style::default().fg(self.config.colorscheme.primary).dim()
            };

            addr_text
                .lines
                .push(Line::from(format!("{row_start:08X}").set_style(addr_style)));

            let mut hex_line = Vec::new();
            let mut ascii_line = Vec::new();

            for j in 0..16 {
                let pos = row_start + j - offset;
                if pos > self.data.len() {
                    break;
                }

                let cursor_here = i == self.cursor_y && j == self.cursor_x;
                let editing = matches!(self.state, AppState::Edit) && cursor_here;

                let span = if editing && offset == 0 {
                    offset = self.is_inserting as usize;

                    ascii_line.push(" ".bg(self.config.colorscheme.primary));

                    Span::from(format!("{}{}", self.buffer[0], self.buffer[1]))
                        .fg(self.config.colorscheme.primary)
                        .reversed()
                } else if pos < self.data.len() {
                    let byte = Byte::new(self.data[pos as usize]);
                    let mut style = byte.get_style(&self.config);
                    style = if cursor_here {
                        match self.is_selecting {
                            false => style.reversed(),
                            true => style.fg(self.config.colorscheme.primary).reversed(),
                        }
                    } else {
                        match self.is_selecting {
                            false => style,
                            true => {
                                let (x, y) = self.selection_range();
                                if x <= pos && pos <= y {
                                    style
                                        .bg(self.config.colorscheme.select)
                                        .fg(self.config.colorscheme.primary)
                                } else {
                                    style
                                }
                            }
                        }
                    };
                    ascii_line
                        .push(Span::from(byte.get_char(&self.config).to_string()).set_style(style));
                    byte.get_hex().set_style(style)
                } else if cursor_here {
                    Span::from("  ")
                        .fg(self.config.colorscheme.primary)
                        .reversed()
                } else {
                    continue;
                };

                hex_line.push(span);

                // spacing

                let spacing = if j == 7 {
                    "  "
                } else if j < 15 {
                    " "
                } else {
                    ""
                };

                hex_line.push(match self.is_selecting {
                    true => {
                        let (x, y) = self.selection_range();
                        if x <= pos && pos < y {
                            spacing.bg(self.config.colorscheme.select).into()
                        } else {
                            spacing.into()
                        }
                    }
                    _ => spacing.into(),
                })
            }

            hex_text.lines.push(Line::from(hex_line));
            ascii_text.lines.push(Line::from(ascii_line));
        }

        frame.render_widget(Paragraph::new(addr_text), columns[0]);
        frame.render_widget(
            Paragraph::new(hex_text).block(
                Block::new()
                    .borders(Borders::LEFT | Borders::RIGHT)
                    .border_style(Style::default().fg(self.config.colorscheme.border))
                    .padding(Padding::horizontal(1)),
            ),
            columns[1],
        );
        frame.render_widget(Paragraph::new(ascii_text), columns[2]);
    }

    fn render_help_popup(&self, frame: &mut Frame, area: Rect) {
        let accent = self.config.colorscheme.accent;
        let primary = self.config.colorscheme.primary;

        let lines = vec![
            Line::from(vec![
                Span::styled("h", Style::default().fg(accent)),
                Span::styled(" - help      ", Style::default().fg(primary)),
                Span::styled("u", Style::default().fg(accent)),
                Span::styled(" - undo     ", Style::default().fg(primary)),
                Span::styled("v", Style::default().fg(accent)),
                Span::styled(" - select", Style::default().fg(primary)),
            ]),
            Line::from(vec![
                Span::styled("q", Style::default().fg(accent)),
                Span::styled(" - quit      ", Style::default().fg(primary)),
                Span::styled("U", Style::default().fg(accent)),
                Span::styled(" - redo     ", Style::default().fg(primary)),
                Span::styled("y", Style::default().fg(accent)),
                Span::styled(" - copy", Style::default().fg(primary)),
            ]),
            Line::from(vec![
                Span::styled("i", Style::default().fg(accent)),
                Span::styled(" - insert    ", Style::default().fg(primary)),
                Span::styled("s", Style::default().fg(accent)),
                Span::styled(" - save     ", Style::default().fg(primary)),
                Span::styled("p", Style::default().fg(accent)),
                Span::styled(" - paste", Style::default().fg(primary)),
            ]),
            Line::from(vec![
                Span::styled("bs", Style::default().fg(accent)),
                Span::styled(" - delete   ", Style::default().fg(primary)),
                Span::styled("pgup,pgdn", Style::default().fg(accent)),
                Span::styled(" - move screen", Style::default().fg(primary)),
            ]),
        ];

        let popup = Paragraph::new(Text::from(lines)).block(
            Block::bordered()
                .border_type(ratatui::widgets::BorderType::Rounded)
                .fg(primary)
                .padding(Padding::symmetric(1, 0))
                .title_top(Line::from(vec![
                    //Span::styled("──── ", Style::default().fg(primary)),
                    Span::styled(" help ", Style::default().fg(accent)),
                ])),
        );

        let popup_layout = Layout::default()
            .direction(Direction::Horizontal)
            .flex(Flex::End)
            .constraints(vec![Constraint::Length(41)])
            .split(area);

        let popup_layout = Layout::default()
            .direction(Direction::Vertical)
            .flex(Flex::End)
            .constraints(vec![Constraint::Length(6)])
            .split(popup_layout[0]);

        frame.render_widget(Clear, popup_layout[0]);
        frame.buffer_mut().set_style(
            popup_layout[0],
            Style::default().bg(self.config.colorscheme.background),
        );
        frame.render_widget(popup, popup_layout[0]);
    }
}

```

### File: src\app\state.rs
```rs
use super::change::Change;
use crate::config::Config;
use clap::Parser;
use color_eyre::Result;
use ratatui::DefaultTerminal;
use std::{fs::File, io::Read, path::Path};

#[derive(Parser, Debug)]
#[command(version, about)]
pub struct Args {
    pub file: String,
}

#[derive(Debug, PartialEq, Eq)]
pub enum AppState {
    Move,
    Edit,
    Help,
}

pub struct App {
    pub config: Config,
    pub file_name: String,
    pub data: Vec<u8>,
    pub starting_line: usize,
    pub cursor_x: usize,
    pub cursor_y: usize,
    pub frame_height: usize,
    pub running: bool,
    pub state: AppState,
    pub buffer: [char; 2],
    pub changes: Vec<Change>,
    pub made_changes: Vec<Change>,
    pub is_inserting: bool,
    pub is_selecting: bool,
    pub selection_start: usize,
    pub clipboard: Vec<u8>,
}

impl App {
    pub fn new(args: Args, config: Config) -> Result<Self> {
        let path = Path::new(&args.file);
        let mut data = Vec::new();

        if path.exists() {
            let mut file = File::open(&args.file)?;
            file.read_to_end(&mut data)?;
        }

        Ok(Self {
            file_name: args.file,
            running: true,
            data,
            starting_line: 0,
            cursor_x: 0,
            cursor_y: 0,
            frame_height: 0,
            state: AppState::Move,
            buffer: [' ', ' '],
            changes: Vec::new(),
            made_changes: Vec::new(),
            config,
            is_inserting: false,
            is_selecting: false,
            selection_start: 0,
            clipboard: Vec::new(),
        })
    }
    pub fn run(mut self, mut terminal: DefaultTerminal) -> Result<()> {
        self.running = true;
        while self.running {
            terminal.draw(|frame| self.render(frame))?;
            self.handle_crossterm_events()?;
            //maybe this will become an update() func if i need more stuff
            self.set_startingline();
        }
        Ok(())
    }
}

```

### File: src\app\utils.rs
```rs
use std::{fs::File, io::Write};

use crate::app::App;

impl App {
    pub fn quit(&mut self) {
        self.running = false;
    }
    //starting_line
    pub fn set_startingline(&mut self) {
        if self.cursor_y < self.starting_line + 5 {
            self.starting_line = self.cursor_y.saturating_sub(5);
        }
        if self.cursor_y > self.starting_line + self.frame_height.saturating_sub(1 + 5) {
            self.starting_line = self
                .cursor_y
                .saturating_sub(self.frame_height.saturating_sub(1 + 5));
        }
    }

    //cursor
    pub fn get_idx(&self) -> usize {
        self.cursor_y * 16 + self.cursor_x
    }

    pub fn set_idx(&mut self, idx: usize) {
        self.cursor_y = idx / 16;
        self.cursor_x = idx % 16;
    }

    pub fn move_up(&mut self) {
        self.cursor_y = self.cursor_y.saturating_sub(1);
    }
    pub fn move_down(&mut self) {
        self.cursor_y += 1;
        if self.cursor_y * 16 > self.data.len() {
            self.cursor_y -= 1;
        }
    }
    pub fn move_page_up(&mut self) {
        self.cursor_y = self.cursor_y.saturating_sub(self.frame_height);
    }
    pub fn move_page_down(&mut self) {
        self.cursor_y += self.frame_height;
        if self.cursor_y * 16 > self.data.len() {
            self.cursor_y -= self.frame_height;
        }
    }
    pub fn move_right(&mut self) {
        self.cursor_x += 1;
        if self.get_idx() >= self.data.len() + 1 {
            self.cursor_x -= 1;
        }
        if self.cursor_x >= 16 {
            self.cursor_x = 0;
            self.cursor_y += 1;
        }
    }
    pub fn move_left(&mut self) {
        if self.cursor_x == 0 {
            if self.cursor_y == 0 {
                return;
            }
            self.cursor_x = 15;
            self.cursor_y = self.cursor_y.saturating_sub(1);
        } else {
            self.cursor_x -= 1;
        }
    }

    //selection
    pub fn selection_range(&self) -> (usize, usize) {
        if !self.is_selecting {
            return (self.get_idx(), self.get_idx());
        }
        (
            self.get_idx().min(self.selection_start),
            self.get_idx()
                .max(self.selection_start)
                .min(self.data.len() - 1),
        )
    }

    pub fn get_selection_data(&self) -> Vec<u8> {
        let (x, y) = self.selection_range();
        self.data[x..(y + 1)].to_vec()
    }

    //buffer
    pub fn insert_to_buffer(&mut self, c: char) {
        let c = c.to_ascii_uppercase();
        if self.buffer[0] == ' ' {
            self.buffer[0] = c;
        } else if self.buffer[1] == ' ' {
            self.buffer[1] = c;
        }
    }

    pub fn buffer_to_u8(&self) -> u8 {
        let mut s = String::new();
        s.push(self.buffer[0]);
        s.push(self.buffer[1]);
        u8::from_str_radix(&s, 16).unwrap()
    }

    //data functions
    pub fn replace_data(&mut self, idx: usize, new: Vec<u8>) {
        for (i, b) in new.iter().enumerate() {
            let pos = idx + i;
            if pos < self.data.len() {
                self.data[pos] = *b;
            } else {
                self.data.push(*b);
            }
        }
    }

    pub fn insert_data(&mut self, idx: usize, new: Vec<u8>) {
        for (i, b) in new.iter().enumerate() {
            self.data.insert(idx + i, *b);
        }
    }

    pub fn delete_data(&mut self, idx: usize, amt: usize) {
        for _ in 0..amt {
            if idx < self.data.len() {
                self.data.remove(idx);
            } else {
                break;
            }
        }
    }

    pub fn save(&mut self) {
        File::create(self.file_name.clone())
            .unwrap()
            .write_all(&self.data)
            .unwrap();
    }
}

```

