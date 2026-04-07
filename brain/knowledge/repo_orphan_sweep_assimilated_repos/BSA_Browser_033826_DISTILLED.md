---
id: BSA_Browser
type: knowledge
owner: OA_Triage
---
# BSA_Browser
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
## BSA Browser

### Introduction
BSA Browser is a Bethesda Archive browser & extractor application for Windows. Games that are supported includes the Fallout series and Elder Scrolls series (except Elder Scrolls Online).

BSA Browser started as a fork of [Fallout Mod Manager](https://sourceforge.net/projects/fomm/)'s BSA Browser as a standalone application & has been steadily improved with more features.

Read more at [BSA Browser](https://www.nexusmods.com/skyrimspecialedition/mods/1756) on Nexus Mods.

Requires .NET Framework 4.8

### Features
 - Browse & extract files from .BSA/.BA2/.DAT archives
 - Browse multiple archive files simultaneously
 - Drag & drop for opening archives and extracting
 - File search, with wildcard and regex support
 - Preview supported files with built-in tools. And for all other files open with the default system application
 - Recent Files list
 - Setup quick exporting for frequently used paths (See Tools -> Options)
 - Copy full path, folder path or file name
 - Compare archives, see new, changed or removed files
 - Supports PS4 modding (Though untested by me)
 
### Forked Version
Fork is based on Fallout Mod Manager [v0.13.21](https://sourceforge.net/p/fomm/code/685/tree/branches/qfomm/)

### License and Copyright
[Fallout Mod Manager](https://sourceforge.net/projects/fomm/) is licensed under GPLv3.

All rights on source code and libraries belong to their respective owners.

### Credits
- Thanks to Timeslip, Q & kaburke for [Fallout Mod Manager](https://sourceforge.net/projects/fomm/)
- Thanks to [SockNastre](https://github.com/SockNastre) for the help with GNF support
- [bsaopt](https://github.com/Ethatron/bsaopt)
- [BA2Lib](https://github.com/digitalutopia1/BA2Lib)
- [F4SE's ba2extract tool](http://f4se.silverlock.org/)
- [B.A.E. - Bethesda Archive Extractor](http://www.nexusmods.com/fallout4/mods/78)

```

### File: BSA Browser CLI\README.md
```md
# BSA Browser CLI

This is a CLI program to interact with BSA/BA2 archives, created by request.

```

### File: CHANGELOG.txt
```txt
[1.17.0]

- Added right click menu options to remove all loaded or unloaded archives
- Added support for B5G6R5_UNORM textures
- BSA Browser will now attempt to translate hashes in Morrowind.bsa archives without name table (e.g. Xbox)
- CLI: Added --exclude option, same as -f option but opposite
- CLI: Multiple filters can now be defined and mixed (simple, exclude, regex). Runs from first to last
- CLI: Added sub option to -l to display filename only
- CLI: Added sub option to -l to humanize file size
- CLI: Added sub option to -e to extract files directly into destination, without directories

[1.16.0]

- Added options to enable/disable file association and shell integration in Options. Will prompt for administrative rights if it doesn't already have
- Added option to reset settings if upgrading settings (after an update) fails
- Added proper file check for unloaded archives
- Added unsupported textures message box which lists the unsupported files
- Added ability to cancel extraction started from Windows Explorer context menu
- Disallow running batch scripts automatically when built-in preview is disabled, for safety reasons
- Fixed progress dialog not updating and freezing when extracting from Explorer context menu

[1.15.1]

- Fixed extraction button and context menu not working (only drag & drop worked)

[1.15.0]

- Added progress dialog when opening multiple archives (currently when opening more than 3 at a time, but open to suggestions)
- Added ability to cancel opening archives in new progress dialog
- Added 'All files' label before extract buttons to hopefully indicate behaviour bit clearer
- Added archive path and file size in tool tip when hovering over archive in tree view
- Added new setting to remember open archives, will be shown as transparent to indicate it's not currently loaded
- Added support for BC6H_UF16 format
- Added option to set a max resolution for previews, default value is 1024x1024. Helps with performance, especially when resizing the window
- Allow multiple previews at a time
- Added ability to reorder archives in tree view
- Improved opening & closing archives performance, especially if they have a lot of files
- Improved performance of Preview window during resizing
- Removed 'Preview' button
- Moved 'Options' to 'Tools' menu
- Updated .NET Framework to 4.8

[1.14.1]

- Fixed extracting, accidentally broke a lot of it in 1.14.0

[1.14.0]

- Added better error message for when opening Archives fails
- Added "Reload" context option to archives
- Added "Open Containing Folder" context option to archives
- Optimized Compare tool, it's now a lot faster, more memory efficient and more accurate (one file went from 1000ms to 90ms compare time)
- More compact Compare tool UI, more space for the list
- Added searching to Compare tool
- Added type filters (Unique, Changed, Identical) to Compare tool
- Added directory filtering to Compare tool
- Added previewing to Compare tool
- Added extracting to Compare tool
- Files are now sorted by file path then type in Compare tool
- Added more properties to compare for GNF textures in Compare Entry tool
- Fixed first level of folders not being sorted corretly in archive tree

[1.13.1]

- Added options to "Extract here" and "Extract to directory" for right click context menu in Explorer
- Added check to prevent extracting same archive multiple times at the same time
- Changed behaviour to now be able to do multiple extractions at the same time, but limited to one per archive
- Main window will no longer be locked when extracting
- Fixed issues with trying to use Extract right click context menu in Explorer when BSA Browser is already open
- Fixed issues with opening main window when a extracting operation is in progress
- Fixed not closing properly when using right click context menu in Explorer in some scenarios
- Fixed program crashing when opening archive causes an error. Will now just show error message
- Fixed SSL issue when checking for update

[1.13.0]

- Added "All" node in archive list that will show all files in all archives at once
- Added "Archive" column to identify which archive the file is contained in, useful when using the "All" node above
- Added Compare tool. Right click an entry and select Compare, then select one or more entries to compare against. Does a byte to byte comparison and compares some texture property currently, can add more by request if anyone have ideas
- Added support for XboxDDS. After extract you will need to convert the file with xtexconv yourself
- Added hotkey combination to reset settings during startup. Hold [Ctrl] + [Alt] + [Shift] before and during startup. Message will be shown if successful
- Added support for Morrowind archives without name tables (for example for Xbox)
- Added /extract flag to immediately extract archive to new folder with same name as archive
- Added option to installer to add a "Extract with BSA Browser" to Explorer context menu to immediately extract
- Prepend filenames with index in Archives without string table, mostly for sorting purposes
- Include extension in filenames in Archives without string table (when available)
- Include directory hash in filenames in Archives without string table (when available)
- Replace DDS extension with GNF during previewing if enabled
- Fixed showing files from multiple folders when folders have similar names, like 'folder' & 'folder2'
- Fixed slightly incorrect filesizes in BA2 texture Archives
- Fixed cubemap extraction

[1.12.4]

- Fixed startup crash after last closing the program while minimized

[1.12.3]

- Fixed DDS previewing. Forgot the Pfim DLL, whoops....
- Improve parsing speed of the "Always show uncompressed file size" option slightly
- Added option to match last changed date with archive
- Added option to replace .dds extensions for PS4 textures with .gnf, so you can associate a different program for these

[1.12.2]

- Improved DPI scaling
- Fixed hangup when cancelling an extraction

[1.12.1]

- Fixed incorrect display file size on uncompressed files when enabling the "Always show uncompressed file size" option

[1.12.0]

- Added icons for file list and folder tree with options to disable them individually
- Added texture information in Title of the DDS preview window
- Added .bat files to supported formats for Text Previewer
- Added confirmation message for emptying recents list
- Added extraction speed to progress dialog
- Improved/fixed previewing of F4/Skyrim/F76 textures using Pfim: https://github.com/nickbabcock/Pfim
- Improved previewing files outside of built-in viewers, files without extension and without any associated programs will now automatically prompt the "Open with" window
- Reset user settings for previewing because of above change, make sure to check them again if needed
- Removed ATI header options for textures, default behaviour now because GIMP/Paint.net etc can open these textures now
- Tweaked font size a bit
- Updated .NET Framework to 4.7.2
- Updated SharpZipLib from 1.1.0 to 1.2.0
- Updated IonKiwi.lz4.net from 1.0.12 to 1.0.15
- Fixed <Files> nodes not working correctly for some archives
- Fixed application starting outside of viewable bounds, appearing only in taskbar. Now the top left point of the window will always be visible
- Fixed saving stack traces to containing folder. If program doesn't have access to it (for example when installing in Program Files) write to '%appdata%\BSA Browser' folder instead
- Fixed some files not appearing because of mismatched casing
- Fixed "Always use real file size" option not working at all, and changed the text
- CLI: Added --noheaders option to extract unsupported textures without DDS header instead of skipping
- CLI: Added --overwrite option to overwrite existing files. Default behavior is to skip existing files now. Thanks to Wynadorn
- CLI: Removed --ati option for same reason stated above

[1.11.0]

- Added DXGI_FORMAT_B8G8R8X8_UNORM as supported format
- Added option to disable check for updates
- Added 'Reset to Default' button to Options
- Added prompt to extract unsupported textures in BA2 archives without generated DDS header for advanced users
- Added Discord link in menu
- Any file can now be previewed by passing it off to OS if there isn't a built-in tool
- Additionally, added tab in Options where you can disable built-in tool for specific file types
- Additionally 2, textures that are supported but can't be previewed with the built-in one will be passed off to the system default (GIMP, Paint.net etc)
- Fixed creating multiple nodes for same folder because of upper/lower case
- Fixed Options tab order

[1.10.0]

- Added specific error for when reading name table fails, which will inform you to try another encoding
- Fixed not being able to drag open archives with upper casing extension
- CLI: Added option to set encoding
- CLI: Added -i option to ignore errors
- CLI: Allow hyphens and slashes for options
- CLI: Allow colon and equals sign for sub-options (-l for example)
- CLI: Make use of exit codes
- CLI: Removed encoding being printed to console

[1.9.9]

- Added <Files> nodes to directories that only shows files directly under it, excluding sub directories
- Added text previewer. Including syntax highlighting for .JSON and .XML
- Added option to set encoding. Useful for non-english environments. Be careful with this
- Added licenses for third party libraries (should have been there from the start)
- Added .NIF to previewing in default program
- Updated to .NET Framework 4.6
- Updated copyright years
- Improved window state saving
- Fixed requiring specific VC++ versions
- Fixed crash in CLI when trying to set console cursor when one isn't available. Thanks to Bioruebe

[1.9.8]

- More detailed report when files fail to extract
- Fixed opening archives containing special characters in file names 

[1.9.7]

- Fixed broken extraction for many BSA archives
- Added links to Fallout 4 and Skyrim Nexus Pages and to GitHub in Help menu
- All unhandled exceptions are now saved to 'stack traces' folder. Useful when reporting bugs
- CLI: Defaults to list (/l) option

[1.9.6]

- Added option to set max recent files
- Changed file list font to Segoe UI
- Updated the progress dialog appearance. The ETA isn't super accurate, but best I can do atm. It's going to be improved
- Increased Morrowind archive reading speed by up to 387.587% (7s average -> 1.5s average reading the Morrowind.bsa 100 times)
- Fixed error opening some archives caused by always using system default encoding. This caused errors on some systems, for example systems set to Japanese locale

[1.9.5]

Note: Previews are getting outdated, many Fallout 76 textures show incorrectly or don't work at all. Gonna look into updating, but it's not my code so not familiar with it yet

- Implemented DX10 headers for Fallout 76. GIMP DDS support isn't great for Fallout 76, so you might wanna look into Photoshop or other tools
- Changed how errors are handled during extraction. Extraction continues and a report is written in the destination
- Updated Progress window
- Fixed BA2 textures being extracted with null bytes at the end
- Fixed being able to click extract while one is already active by blocking main window during

[1.9.1]

- Fixed some textures causing invalid DDS header error

[1.9]

- Very early Fallout 76 support
- Added tool to compare archives. See what has been added, removed or changed
- Removed "This archive is already opened" message. Bring window to front instead
- Fixed rare decompress error with certain files (e.g. True Storms, Skyland)

[1.8.5]

- Added support for GNF format .ba2
- Added "Extract Archives..." menu option to extract multiple archives at once
- Fix crash when sorting without any archives open

[1.8]

- Added right click menu options for archives to extract entire archive
- Added drag-and-drop for opening archives
- Added .bmp, .png, .jpg preview
- Added .psc preview. Opens in default program
- Added CLI tool to interact with archives. Available as an option in installer
- Improved browsing speed. Much less hang-ups when browsing big files
- Changed extract buttons behaviour. They will now only ever extracts files/folders currently listed, for example to extract only searched files or only files in a folder
- Changed sorting behaviour. Sort by clicking columns instead of combobox
- Fixed .DDS preview for Oblivion
- Support unicode characters in file names
- Updated lz4 library from 1.0.5 to 1.0.9

[1.7]

- Added built-in previewer for .DDS files

[1.6.5]

- Right click menu now has 'Extract' and 'Extract Folders' buttons for selected files
- Buttons above search bar now has 'Extract all' and 'Extract all folders'
- New 'Select All' menu item
- Move copy menu items into cascading 'Copy' menu

[1.6.1]

- Fix support for older games that was broken in 1.6

[1.6]

- Added support for Skyrim Special Edition .BSA archives

[1.5.2]

- Added "Close All Archives" menu button
- Fixed "Cancel" button being unresponsive
- Removed Offset sorting option
- Scroll to top when switching sub folder in archives
- Fixed program crashing when not able to check for updates (e.g. blocked by firewall)

[1.5.1]

- Added option for ATI header for textures. More accurate, but only seems to work for Photoshop plugin
- Fixed files being extracted empty (i.e. filled with zeros)

[1.5]

- Added support for .BA2 (Fallout 4) archive files. Comes with the same limitations as other tools, I.E. normal maps aren't accurate. For more information download the Fallout 4 tools from http://f4se.silverlock.org/ & read the ba2extract note in the readme
- Added "Check for update" & very small update notifier. Just adds an "(!)" to Help menu if there is an update
- Allow opening multiple files at once
- Full file path now shown in recent files, since Fallout 3 & NV share file names
- Also show a F3/NV tag next to archive name if it's a original (i.e. not a mod/dlc) Fallout 3 or New Vegas file
- Removed extra columns & related option. Only filename & file size columns now
- Fixed opening the same file multiple times. Not allowed anymore

[1.4.2]

- Fix "Header checksum illegal" error
- Fix some out of range errors

[1.4.1]

- Fix missing DLL error

[1.4]

- Improved list performance, everything should be a bit faster now
- Allow wild card in normal search
- Add option for more columns (File size, offset, compressed)
- Add shortcuts to open quick extract paths
- Regex preference is now remembered
- Search term will now appear red if it's invalid
- Fix lag when searching, by adding a small delay

[1.3.1]

- Fixed window appearing outside the screen's working area

[1.3]

- Add option to sort BSA directories
- Add option to toggle maintaining folder structure when using "Extract" button
- Ctrl + A to select all list items

[1.2]

- Add currently shown files counter
- Add ability to create custom quick extract paths
- Show extracting progress in title
- Improve folder browser dialog
- Enable visual styles for Options list
... [TRUNCATED]
```

### File: TODO.md
```md
### ToDo

- [ ] Detailed view for advanced mode or debug mode
- [ ] Include xtexconv for converting XboxDDS to DDS
- [ ] Define workspaces (Undecided)

### Complete

- [X] ~~Fix estimated extraction time~~
- [X] ~~Ability to view texture compression type (for example in Title for preview window) https://forums.nexusmods.com/index.php?showtopic=4997660/#entry77156298~~
- [X] ~~Fix previewing files without extension using ShellExecuteEx with openas~~
- [X] ~~Extract GNF with .gnf extension instead of .dds so it can be associated with a different program by the OS~~
- [X] ~~Option to match time stamp of extracted files with the archive~~
- [X] ~~Search across all open archives (maybe a 'All' node)~~
- [X] ~~Right click options in Explorer to extract~~
- [X] ~~Compare single files within any archive. Idea: Right click to mark first file, then right click second file to start comparing. Display the filename of first file when selecting the second (\{archive\} - \{filename\})~~
- [X] ~~And/or: Same as above, but second file can be multiple files and they're all compared to the first~~
- [X] ~~Properly handle shutdown when extract operations are active~~
- [X] ~~Compare tool: Toggle overlapping files (only show different files) OR check boxes for each type~~
- [X] ~~Compare tool: Improve sorting~~
- [X] ~~Compare tool: Add ability to preview files~~
- [X] ~~Compare tool: Add ability to extract files~~
- [X] ~~Compare tool: Add option to extract entire side regardless of selection~~
- [X] ~~Compare tool: Change existing Extract to specify it's selected files only~~
- [X] ~~Compare tool: Async comparing, show progress in title~~
- [X] ~~Compare tool: Compare only files under specified nodes~~
- [X] ~~Remember opened archives, list in archive tree but unloaded (Undecided)~~
- [X] ~~Preview max starting size, for example scale everything above 1080p to 1080p~~
- [X] ~~Preview loading cursor during load~~
- [X] ~~Allow multiple previews at a time~~
- [X] ~~Option to install and uninstall shell context menu integration~~
- [X] ~~Allow multiple extraction operations at same time (maybe limit to one per archive or actually check indiviual files)~~
- [X] ~~CLI: Allow defining multiple filters/regex (including combining simple and regex), run each filter one after another.~~
- [X] ~~CLI: Exclude simple filter~~

```

### File: .github\7z_filelist.txt
```txt
"..\BSA Browser\bin\Release\BSA Browser.exe"
"..\BSA Browser\bin\Release\BSA Browser.exe.config"
"..\BSA Browser\bin\Release\ICSharpCode.SharpZipLib.dll"
"..\BSA Browser\bin\Release\ICSharpCode.TextEditor.dll"
"..\BSA Browser\bin\Release\lz4.AnyCPU.loader.dll"
"..\BSA Browser\bin\Release\Pfim.dll"
"..\BSA Browser\bin\Release\Sharp.BSA.BA2.dll"
"..\BSA Browser\bin\Release\System.Management.Automation.dll"
"..\BSA Browser CLI\bin\Release\bsab.exe"
"..\Licenses"
```

### File: BSA Browser\AboutBox.cs
```cs
﻿using System;
using System.Reflection;
using System.Windows.Forms;

namespace BSA_Browser
{
    partial class AboutBox : Form
    {
        public AboutBox()
        {
            InitializeComponent();
            this.Text = String.Format("About {0}", AssemblyTitle);
            this.labelProductName.Text = AssemblyProduct;
            this.labelVersion.Text = String.Format("Version {0}", Program.Version);
            this.labelCopyright.Text = AssemblyCopyright;
            this.labelCompanyName.Text = AssemblyCompany;
        }

        #region Assembly Attribute Accessors

        public string AssemblyTitle
        {
            get
            {
                object[] attributes = Assembly.GetExecutingAssembly().GetCustomAttributes(typeof(AssemblyTitleAttribute), false);
                if (attributes.Length > 0)
                {
                    AssemblyTitleAttribute titleAttribute = (AssemblyTitleAttribute)attributes[0];
                    if (titleAttribute.Title != "")
                    {
                        return titleAttribute.Title;
                    }
                }
                return System.IO.Path.GetFileNameWithoutExtension(Assembly.GetExecutingAssembly().CodeBase);
            }
        }

        public string AssemblyDescription
        {
            get
            {
                object[] attributes = Assembly.GetExecutingAssembly().GetCustomAttributes(typeof(AssemblyDescriptionAttribute), false);
                if (attributes.Length == 0)
                {
                    return "";
                }
                return ((AssemblyDescriptionAttribute)attributes[0]).Description;
            }
        }

        public string AssemblyProduct
        {
            get
            {
                object[] attributes = Assembly.GetExecutingAssembly().GetCustomAttributes(typeof(AssemblyProductAttribute), false);
                if (attributes.Length == 0)
                {
                    return "";
                }
                return ((AssemblyProductAttribute)attributes[0]).Product;
            }
        }

        public string AssemblyCopyright
        {
            get
            {
                object[] attributes = Assembly.GetExecutingAssembly().GetCustomAttributes(typeof(AssemblyCopyrightAttribute), false);
                if (attributes.Length == 0)
                {
                    return "";
                }
                return ((AssemblyCopyrightAttribute)attributes[0]).Copyright;
            }
        }

        public string AssemblyCompany
        {
            get
            {
                object[] attributes = Assembly.GetExecutingAssembly().GetCustomAttributes(typeof(AssemblyCompanyAttribute), false);
                if (attributes.Length == 0)
                {
                    return "";
                }
                return ((AssemblyCompanyAttribute)attributes[0]).Company;
            }
        }

        #endregion

        private void LinkLabel_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            LinkLabel linkLabel = (LinkLabel)sender;

            try
            {
                System.Diagnostics.Process.Start((string)linkLabel.Tag);
            }
            catch (Exception)
            {
                MessageBox.Show(this, "Couldn't open link.");
            }
        }
    }
}

```

### File: BSA Browser\AboutBox.Designer.cs
```cs
﻿namespace BSA_Browser
{
    partial class AboutBox
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(AboutBox));
            this.logoPictureBox = new System.Windows.Forms.PictureBox();
            this.labelProductName = new System.Windows.Forms.Label();
            this.labelVersion = new System.Windows.Forms.Label();
            this.labelCopyright = new System.Windows.Forms.Label();
            this.labelCompanyName = new System.Windows.Forms.Label();
            this.okButton = new System.Windows.Forms.Button();
            this.tabControl1 = new System.Windows.Forms.TabControl();
            this.tabPage1 = new System.Windows.Forms.TabPage();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.linkLabel2 = new System.Windows.Forms.LinkLabel();
            this.label2 = new System.Windows.Forms.Label();
            this.linkLabel1 = new System.Windows.Forms.LinkLabel();
            this.label1 = new System.Windows.Forms.Label();
            this.tabPage2 = new System.Windows.Forms.TabPage();
            this.txtLicense2 = new System.Windows.Forms.TextBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.lName2 = new System.Windows.Forms.Label();
            this.llLink2 = new System.Windows.Forms.LinkLabel();
            this.lLicense2 = new System.Windows.Forms.Label();
            this.tabPage3 = new System.Windows.Forms.TabPage();
            this.txtLicense3 = new System.Windows.Forms.TextBox();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.lName3 = new System.Windows.Forms.Label();
            this.llLink3 = new System.Windows.Forms.LinkLabel();
            this.tabPage4 = new System.Windows.Forms.TabPage();
            this.txtLicense4 = new System.Windows.Forms.TextBox();
            this.groupBox4 = new System.Windows.Forms.GroupBox();
            this.lName4 = new System.Windows.Forms.Label();
            this.llLink4 = new System.Windows.Forms.LinkLabel();
            this.lLicense4 = new System.Windows.Forms.Label();
            this.tabPage5 = new System.Windows.Forms.TabPage();
            this.txtLicense5 = new System.Windows.Forms.TextBox();
            this.groupBox5 = new System.Windows.Forms.GroupBox();
            this.lName5 = new System.Windows.Forms.Label();
            this.llLink5 = new System.Windows.Forms.LinkLabel();
            this.lLicense5 = new System.Windows.Forms.Label();
            this.tabPage6 = new System.Windows.Forms.TabPage();
            this.label4 = new System.Windows.Forms.Label();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.groupBox6 = new System.Windows.Forms.GroupBox();
            this.label3 = new System.Windows.Forms.Label();
            this.linkLabel3 = new System.Windows.Forms.LinkLabel();
            ((System.ComponentModel.ISupportInitialize)(this.logoPictureBox)).BeginInit();
            this.tabControl1.SuspendLayout();
            this.tabPage1.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.tabPage2.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.tabPage3.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.tabPage4.SuspendLayout();
            this.groupBox4.SuspendLayout();
            this.tabPage5.SuspendLayout();
            this.groupBox5.SuspendLayout();
            this.tabPage6.SuspendLayout();
            this.groupBox6.SuspendLayout();
            this.SuspendLayout();
            // 
            // logoPictureBox
            // 
            this.logoPictureBox.Image = ((System.Drawing.Image)(resources.GetObject("logoPictureBox.Image")));
            this.logoPictureBox.Location = new System.Drawing.Point(12, 12);
            this.logoPictureBox.Name = "logoPictureBox";
            this.logoPictureBox.Size = new System.Drawing.Size(32, 32);
            this.logoPictureBox.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.logoPictureBox.TabIndex = 12;
            this.logoPictureBox.TabStop = false;
            // 
            // labelProductName
            // 
            this.labelProductName.AutoSize = true;
            this.labelProductName.Location = new System.Drawing.Point(50, 12);
            this.labelProductName.Margin = new System.Windows.Forms.Padding(3);
            this.labelProductName.MaximumSize = new System.Drawing.Size(0, 17);
            this.labelProductName.Name = "labelProductName";
            this.labelProductName.Size = new System.Drawing.Size(75, 13);
            this.labelProductName.TabIndex = 19;
            this.labelProductName.Text = "Product Name";
            this.labelProductName.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // labelVersion
            // 
            this.labelVersion.AutoSize = true;
            this.labelVersion.Location = new System.Drawing.Point(50, 31);
            this.labelVersion.Margin = new System.Windows.Forms.Padding(3);
            this.labelVersion.MaximumSize = new System.Drawing.Size(0, 17);
            this.labelVersion.Name = "labelVersion";
            this.labelVersion.Size = new System.Drawing.Size(42, 13);
            this.labelVersion.TabIndex = 0;
            this.labelVersion.Text = "Version";
            this.labelVersion.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // labelCopyright
            // 
            this.labelCopyright.AutoSize = true;
            this.labelCopyright.Location = new System.Drawing.Point(50, 50);
            this.labelCopyright.Margin = new System.Windows.Forms.Padding(3);
            this.labelCopyright.MaximumSize = new System.Drawing.Size(0, 17);
            this.labelCopyright.Name = "labelCopyright";
            this.labelCopyright.Size = new System.Drawing.Size(51, 13);
            this.labelCopyright.TabIndex = 21;
            this.labelCopyright.Text = "Copyright";
            this.labelCopyright.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // labelCompanyName
            // 
            this.labelCompanyName.AutoSize = true;
            this.labelCompanyName.Location = new System.Drawing.Point(50, 69);
            this.labelCompanyName.Margin = new System.Windows.Forms.Padding(3);
            this.labelCompanyName.MaximumSize = new System.Drawing.Size(0, 17);
            this.labelCompanyName.Name = "labelCompanyName";
            this.labelCompanyName.Size = new System.Drawing.Size(82, 13);
            this.labelCompanyName.TabIndex = 22;
            this.labelCompanyName.Text = "Company Name";
            this.labelCompanyName.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // okButton
            // 
            this.okButton.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.okButton.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.okButton.Location = new System.Drawing.Point(576, 426);
            this.okButton.Name = "okButton";
            this.okButton.Size = new System.Drawing.Size(75, 23);
            this.okButton.TabIndex = 24;
            this.okButton.Text = "&OK";
            // 
            // tabControl1
            // 
            this.tabControl1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.tabControl1.Controls.Add(this.tabPage1);
            this.tabControl1.Controls.Add(this.tabPage2);
            this.tabControl1.Controls.Add(this.tabPage3);
            this.tabControl1.Controls.Add(this.tabPage4);
            this.tabControl1.Controls.Add(this.tabPage5);
            this.tabControl1.Controls.Add(this.tabPage6);
            this.tabControl1.Location = new System.Drawing.Point(12, 88);
            this.tabControl1.Name = "tabControl1";
            this.tabControl1.SelectedIndex = 0;
            this.tabControl1.Size = new System.Drawing.Size(640, 332);
            this.tabControl1.TabIndex = 28;
            // 
            // tabPage1
            // 
            this.tabPage1.Controls.Add(this.textBox1);
            this.tabPage1.Controls.Add(this.groupBox1);
            this.tabPage1.Controls.Add(this.label1);
            this.tabPage1.Location = new System.Drawing.Point(4, 22);
            this.tabPage1.Name = "tabPage1";
            this.tabPage1.Padding = new System.Windows.Forms.Padding(12, 6, 12, 6);
            this.tabPage1.Size = new System.Drawing.Size(632, 306);
            this.tabPage1.TabIndex = 0;
            this.tabPage1.Text = "BSA Browser";
            this.tabPage1.UseVisualStyleBackColor = true;
            // 
            // textBox1
            // 
            this.textBox1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.textBox1.BackColor = System.Drawing.SystemColors.Window;
            this.textBox1.Font = new System.Drawing.Font("Consolas", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.textBox1.Location = new System.Drawing.Point(15, 76);
            this.textBox1.Multiline = true;
            this.textBox1.Name = "textBox1";
            this.textBox1.ReadOnly = true;
            this.textBox1.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.textBox1.Size = new System.Drawing.Size(602, 202);
            this.textBox1.TabIndex = 39;
            this.textBox1.Text = resources.GetString("textBox1.Text");
            // 
            // groupBox1
            // 
            this.groupBox1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.groupBox1.Controls.Add(this.linkLabel2);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.linkLabel1);
            this.groupBox1.Location = new System.Drawing.Point(15, 9);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(602, 61);
            this.groupBox1.TabIndex = 38;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Information";
            // 
            // linkLabel2
            // 
            this.linkLabel2.AutoSize = true;
            this.linkLabel2.LinkBehavior = System.Windows.Forms.LinkBehavior.NeverUnderline;
            this.linkLabel2.Location = new System.Drawing.Point(61, 38);
            this.linkLabel2.Margin = new System.Windows.Forms.Padding(12, 3, 3, 3);
            this.linkLabel2.Name = "linkLabel2";
            this.linkLabel2.Size = new System.Drawing.Size(66, 13);
            this.linkLabel2.TabIndex = 35;
            this.linkLabel2.TabStop = true;
            this.linkLabel2.Tag = "http://www.nexusmods.com/fallout4/mods/17061/?";
            this.linkLabel2.Text = "Nexus Mods";
            this.linkLabel2.LinkClicked += new System.Windows.Forms.LinkLabelLinkClickedEventHandler(this.LinkLabel_LinkClicked);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(6, 19);
            this.label2.Margin = new System.Windows.Forms.Padding(3);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(69, 13);
            this.label2.TabIndex = 34;
            this.label2.Text = "BSA Browser";
            // 
            // linkLabel1
            // 
            this.linkLabel1.AutoSize = true;
            this.linkLabel1.LinkBehavior = System.Windows.Forms.LinkBehavior.NeverUnderline;
            this.linkLabel1.Location = new System.Drawing.Point(6, 38);
            this.linkLabel1.Margin = new System.Windows.Forms.Padding(3);
            this.linkLabel1.Name = "linkLabel1";
            this.linkLabel1.Size = new System.Drawing.Size(40, 13);
            this.linkLabel1.TabIndex = 33;
            this.linkLabel1.TabStop = true;
            this.linkLabel1.Tag = "https://github.com/AlexxEG/BSA_Browser";
            this.linkLabel1.Text = "GitHub";
            this.linkLabel1.LinkClicked += new System.Windows.Forms.LinkLabelLinkClickedEventHandler(this.LinkLabel_LinkClicked);
            // 
            // label1
            // 
            this.label1.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 284);
            this.label1.Margin = new System.Windows.Forms.Padding(3);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(187, 13);
            this.label1.TabIndex = 32;
            this.label1.Text = "BSA Browser is licensed under GPLv3";
            // 
            // tabPage2
            // 
            this.tabPage2.Controls.Add(this.txtLicense2);
            this.tabPage2.Controls.Add(this.groupBox2);
            this.tabPage2.Controls.Add(this.lLicense2);
            this.tabPage2.Location = new System.Drawing.Point(4, 22);
            this.tabPage2.Name = "tabPage2";
            this.tabPage2.Padding = new System.Windows.Forms.Padding(12, 6, 12, 6);
            this.tabPage2.Size = new System.Drawing.Size(632, 306);
            this.tabPage2.TabIndex = 1;
            this.tabPage2.Text = "SharpZipLib";
            this.tabPage2.UseVisualStyleBackColor = true;
            // 
            // txtLicense2
            // 
            this.txtLicense2.Anchor = ((S
... [TRUNCATED]
```

### File: BSA Browser\BSABrowser.cs
```cs
﻿using BrightIdeasSoftware;
using BSA_Browser.Classes;
using BSA_Browser.Dialogs;
using BSA_Browser.Enums;
using BSA_Browser.Extensions;
using BSA_Browser.Properties;
using BSA_Browser.Sorting;
using BSA_Browser.Tools;
using SharpBSABA2;
using SharpBSABA2.BA2Util;
using SharpBSABA2.BSAUtil;
using SharpBSABA2.Enums;
using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.ComponentModel;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Management.Automation;
using System.Net;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace BSA_Browser
{
    public partial class BSABrowser : Form
    {
        private const string UpdateMarker = "(!) ";

        int _limitSearchId = LimitedAction.GenerateId();
        OpenFolderDialog _openFolderDialog = new OpenFolderDialog();
        ArchiveFileSorter _filesSorter = new ArchiveFileSorter();
        TreeNodeSorter _nodeSorter = new TreeNodeSorter();
        CompareForm _compareForm;
        string[] _args;
        bool _pauseFiltering = false;

        /// <summary>
        /// Gets the selected <see cref="ArchiveNodeTree"/>.
        /// </summary>
        private ArchiveNodeTree SelectedArchiveNode => tlvFolders.SelectedObject as ArchiveNodeTree;

        /// <summary>
        /// Gets list of <see cref="ArchiveEntry"/> currently visible.
        /// </summary>
        private List<ArchiveEntry> VisibleFiles { get; set; } = new List<ArchiveEntry>();

        private IEnumerable<ArchiveEntry> SelectedNodeFiles { get; set; } = Enumerable.Empty<ArchiveEntry>();

        public BSABrowser()
        {
            InitializeComponent();

            // Fix SSL issue with checking for updates, on Windows 7 at least
            ServicePointManager.Expect100Continue = true;
            ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;

            // Set it here otherwise DPI scaling will not work correctly, for some reason
            this.Menu = mainMenu1;

            // Show application version in title
            this.Text += $" ({Program.Version})";

            var archiveNode = new ArchiveNodeTree(ArchiveNodeTreeType.All, null, "All");
            archiveNode.Loaded = true;
            tlvFolders.AddObject(archiveNode);
            tlvFolders.ContextMenu = archiveContextMenu;

            lvFiles.ContextMenu = contextMenu1;

            // Restore last path for OpenFolderDialog
            if (!string.IsNullOrEmpty(Settings.Default.LastUnpackPath))
                _openFolderDialog.InitialFolder = Settings.Default.LastUnpackPath;

            // Load Recent Files list
            if (Settings.Default.RecentFiles != null)
            {
                foreach (string item in Settings.Default.RecentFiles)
                    this.AddToRecentFiles(item);
            }

            // Load Quick Extract Paths
            Settings.Default.QuickExtractPaths = Settings.Default.QuickExtractPaths ?? new QuickExtractPaths();

            this.LoadQuickExtractPaths();

            // Set lvFiles sorter
            ArchiveFileSorter.SetSorter(Settings.Default.SortType, Settings.Default.SortDesc);

            // Enable visual styles
            tlvFolders.EnableVisualStyles();
            lvFiles.EnableVisualStyles();

            // Set TextBox cue
            txtSearch.SetCue("Search term...");

#if DEBUG
            this.SetupDebugTools();
#endif

            filesImageList.Images.Add("NoAssoc", SystemIcons.FilesNoAssoc);

            foldersImageList.Images.Add(new System.Drawing.Bitmap(16, 16));
            foldersImageList.Images.Add(SystemIcons.FolderSmall);
            foldersImageList.Images.Add(SystemIcons.Files);
            foldersImageList.Images.Add((System.Drawing.Icon)this.Icon.Clone());
            foldersImageList.Images.Add(Resources.all);
            foldersImageList.Images.Add(Resources.unloaded);

            if (Settings.Default.Icons.HasFlag(Enums.Icons.FileList))
            {
                lvFiles.SmallImageList = filesImageList;
            }

            if (Settings.Default.Icons.HasFlag(Enums.Icons.FolderTree))
            {
                tlvFolders.SmallImageList = foldersImageList;
            }

            tlvFolders.CanExpandGetter = (x) =>
            {
                return (x as ArchiveNodeTree).SubNodes.Count > 0;
            };
            tlvFolders.ChildrenGetter = (x) =>
            {
                var node = x as ArchiveNodeTree;
                var children = node.SubNodes.AsEnumerable();

                if (node.ShouldHaveFilesNode)
                    children = children.Prepend(new ArchiveNodeTree(ArchiveNodeTreeType.Files, node, "<Files>", loaded: true));

                return children;
            };
            tlvFolders.FormatCell += (sender, e) =>
            {
                var node = e.Model as ArchiveNodeTree;

                if (node.Type == ArchiveNodeTreeType.All || string.IsNullOrEmpty(txtSearch.Text))
                {
                    e.Item.ForeColor = System.Drawing.SystemColors.ControlText;
                    e.Item.Font = null;
                }
                else if (_pathsWithResults.Contains(node.GetTreePath(false).ToLower()))
                {
                    e.Item.ForeColor = System.Drawing.SystemColors.Highlight;
                    e.Item.Font = null;
                }
                else
                {
                    e.Item.ForeColor = System.Drawing.SystemColors.GrayText;
                    e.Item.Font = new System.Drawing.Font(tlvFolders.Font, System.Drawing.FontStyle.Strikeout);
                }
            };
            tlvFolders.CellToolTipGetter += (column, x) =>
            {
                var archive = (x as ArchiveNodeTree).Archive;

                if (archive is BSA bsa)
                {
                    var header = bsa.Header;

                    if (header is BSAHeader bsaHeader)
                    {
                        return $"Type: BSA\nVersion: {bsaHeader.Version}\nFiles: {bsaHeader.FileCount}";
                    }
                    else if (header is BSAHeaderMW mwHeader)
                    {
                        return $"Type: Morrowind\nVersion: {mwHeader.Version}\nFiles: {mwHeader.FileCount}";
                    }

                    return "Unknown archive type";
                }
                else if (archive is BA2 ba2)
                {
                    var header = ba2.Header;
                    return $"Type: {header.Type}\nVersion: {header.Version}\nFiles: {header.NumFiles}";
                }
                else
                {
                    return "Unknown archive type";
                }
            };

            tlvFolders.EnableVisualStyles();
        }

        #region Debug Tools
#if DEBUG
        private bool _filterOneTexturePerFormat = false;

        /// <summary>
        /// Returns <see cref="Archive"/> with the given file path from <see cref="tvFolders"/>.
        /// </summary>
        private Archive FindArchive(string fullPath)
        {
            return tlvFolders
                .Objects
                .OfType<ArchiveNodeTree>()
                .First(x => x.Archive != null && x.FilePath.ToLower() == fullPath.ToLower()).Archive;
        }

        private void SetupDebugTools()
        {
            lvFiles.Columns.Add("Extra", 200);

            var debugMenuItem = mainMenu1.MenuItems.Add("DEBUG");

            debugMenuItem.MenuItems.Add("Average opening speed of archive", OpeningSpeedAverage_Click);
            debugMenuItem.MenuItems.Add("Average extraction speed of selected file", ExtractionSpeedAverage_Click);
            debugMenuItem.MenuItems.Add("Average extraction speed of files", ExtractionSpeedAverageFiles_Click);
            debugMenuItem.MenuItems.Add("Average extraction speed of files (multi-threaded)", ExtractionSpeedAverageFilesMultiThreaded_Click);
            debugMenuItem.MenuItems.Add("Check if all textures formats are supported", CheckTextureFormats_Click);
            debugMenuItem.MenuItems.Add("Show ProgressForm", ShowProgressForm_Click);
            debugMenuItem.MenuItems.Add("Benchmark DoSearch", BenchmarkDoSearch_Click);
            debugMenuItem.MenuItems.Add("Filter out one BA2 texture per format", FilterOneTexturePerFormat_Click);
            debugMenuItem.MenuItems.Add("Copy texture formats", CopyTextureFormats_Click);
            debugMenuItem.MenuItems.Add("Extract files from a filelist", ExtractFilesFromFilelist_Click);
            debugMenuItem.MenuItems.Add("Get Archive2 dwSurfaceFlags for visible files", GetArchive2SurfaceFlags_Click);
            debugMenuItem.MenuItems.Add("Get textures with > 1 mip maps and cubemap", GetTexturesWithMipMaps_Click);
        }

        private void OpeningSpeedAverage_Click(object sender, EventArgs e)
        {
            if (OpenArchiveDialog.ShowDialog(this) != DialogResult.OK)
                return;

            var skipped = 0;
            var path = OpenArchiveDialog.FileNames[0];

            var sw = new Stopwatch();
            var count = 0;
            var results = new List<long>();

            while (count < 40)
            {
                sw.Restart();

                try
                {
                    var extension = Path.GetExtension(path);
                    var encoding = Encoding.GetEncoding(Settings.Default.EncodingCodePage);

                    switch (extension.ToLower())
                    {
                        case ".bsa":
                        case ".dat":
                            if (SharpBSABA2.BSAUtil.BSA.IsSupportedVersion(path) == false)
                            {
                                goto default;
                            }

                            new SharpBSABA2.BSAUtil.BSA(path, encoding, Settings.Default.RetrieveRealSize);
                            break;
                        case ".ba2":
                            new SharpBSABA2.BA2Util.BA2(path, encoding, Settings.Default.RetrieveRealSize);
                            break;
                        default:
                            skipped++;
                            break;
                    }
                }
                catch
                {
                    skipped++;
                }

                sw.Stop();
                results.Add(sw.ElapsedMilliseconds);
                Console.WriteLine(count + " - " + sw.ElapsedMilliseconds + "ms");
                count++;
            }

            Console.WriteLine($"Average: {results.Sum() / results.Count}ms. {skipped} skipped.");
        }

        private void ExtractionSpeedAverage_Click(object sender, EventArgs e)
        {
            if (lvFiles.SelectedIndices.Count == 0)
                return;

            if (lvFiles.SelectedIndices.Count > 1)
            {
                MessageBox.Show(this, "Can only test one file at a time", "Error");
                return;
            }

            var fe = VisibleFiles[lvFiles.SelectedIndices[0]];
            Stopwatch sw = new Stopwatch();
            int count = 0;
            List<long> results = new List<long>();

            while (count < 1000)
            {
                sw.Restart();
                using (var ms = fe.GetDataStream())
                {
                    sw.Stop();
                    results.Add(sw.ElapsedMilliseconds);
                    count++;
                }
            }

            Console.WriteLine($"Average: {results.Sum() / results.Count}ms");
        }

        private void ExtractionSpeedAverageFiles_Click(object sender, EventArgs e)
        {
            if (tlvFolders.SelectedObject == null)
                return;

            var sw = new Stopwatch();
            int count = 0;
            var results = new List<long>();

            while (count < 50)
            {
                sw.Restart();
                foreach (var file in VisibleFiles)
                    file.GetDataStream();
                sw.Stop();
                results.Add(sw.ElapsedMilliseconds);
                count++;
                Console.WriteLine($"{count} - Average: {results.Sum() / results.Count}ms");
            }

            MessageBox.Show($"Average: {results.Sum() / results.Count}ms");
        }

        private async void ExtractionSpeedAverageFilesMultiThreaded_Click(object sender, EventArgs e)
        {
            if (VisibleFiles.Count == 0)
                return;

            var sw = new Stopwatch();
            int count = 0;
            var results = new List<long>();
            var tasks = new List<Task>();

            var chunks = VisibleFiles.Split(4);

            while (count < 50)
            {
                sw.Restart();

                foreach (var list in chunks)
                {
                    Task task = new Task(files =>
                    {
                        var sharedParams = new Dictionary<string, SharedExtractParams>();
                        foreach (var arc in (files as List<ArchiveEntry>).Select(x => x.Archive.FullPath.ToLower()).Distinct())
                            sharedParams.Add(arc, FindArchive(arc).CreateSharedParams(true, true));

                        foreach (ArchiveEntry file in (List<ArchiveEntry>)files)
                            // file.Extract(@"D:\Testing\test1", true, file.FileName, sharedParams[file.Archive.FullPath.ToLower()]);
                            file.GetDataStream(sharedParams[file.Archive.FullPath.ToLower()]);

                        foreach (var sp in sharedParams)
                            sp.Value.Reader.Close();
                    }, list);

                    tasks.Add(task);
                    task.Start();
                }

                await Task.WhenAll(tasks);
                sw.Stop();
                results.Add(sw.ElapsedMilliseconds);
                count++;
                Console.WriteLine($"{count} - Average: {results.Sum() / results.Count}ms");
                tasks.Clear();
            }

            MessageBox.Show($"Average: {results.Sum() / results.Count}ms");
        }

        private void CheckTextureFormats_Click(object sender, EventArgs e)
        {
            int checkedTextures = 0;
            int unsupported = 0;
            var sw = new Stopwatch();

            sw.Start();

            foreach (var fe in VisibleFiles.OfType<BA2TextureEntry>())
            {
                checkedTextures++;

                if (!fe.IsFormatSupported())
                    unsupported++;
            }

            sw.Stop();
            MessageBox.Show($"Checked {checkedTextures} textures in {sw.ElapsedMilliseconds}ms, {unsupported} unsupported textures.");
        }

        private void ShowProgressForm_Click(object sender, EventArgs e)
        {
            ProgressForm pf = new ProgressForm(10);
            pf.Show(this);

       
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
