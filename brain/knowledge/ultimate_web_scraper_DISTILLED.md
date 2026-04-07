---
id: ultimate-web-scraper
type: knowledge
owner: OA_Triage
---
# ultimate-web-scraper
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
Ultimate Web Scraper Toolkit
============================

A PHP library of tools designed to handle all of your web scraping needs under a MIT or LGPL license.  This toolkit easily makes RFC-compliant web requests that are indistinguishable from a real web browser, has a web browser-like state engine for handling cookies and redirects, and a full cURL emulation layer for web hosts without the PHP cURL extension installed.  The powerful tag filtering library TagFilter is included to easily extract the desired content from each retrieved document or used to process HTML documents that are offline.

This tookit also comes with classes for creating custom web servers and WebSocket servers.  That custom API you want the average person to install on their home computer or deploy to devices in the enterprise just became easier to deploy.

[![Donate](https://cubiclesoft.com/res/donate-shield.png)](https://cubiclesoft.com/donate/) [![Discord](https://img.shields.io/discord/777282089980526602?label=chat&logo=discord)](https://cubiclesoft.com/product-support/github/)

Features
--------

* Carefully follows the IETF RFC Standards surrounding the HTTP protocol.
* Supports file transfers, SSL/TLS, and HTTP/HTTPS/CONNECT proxies.
* Easy to emulate various web browser headers.
* A web browser-like state engine that emulates redirection (e.g. 301) and automatic cookie handling for managing multiple requests.
* HTML form extraction and manipulation support.  No need to fake forms!
* Extensive callback support.
* Asynchronous/Non-blocking socket support.  For when you need to scrape lots of content simultaneously.
* WebSocket support.
* A full cURL emulation layer for drop-in use on web hosts that are missing cURL.
* An impressive CSS3 selector tokenizer (TagFilter::ParseSelector()) that carefully follows the W3C Specification and passes the official W3C CSS3 static test suite.
* Includes a fast and powerful tag filtering library (TagFilter) for correctly parsing really difficult HTML content (e.g. Microsoft Word HTML) and can easily extract desired content from HTML and XHTML using CSS3 compatible selectors.
* TagFilter::HTMLPurify() produces XSS defense results on par with HTML Purifier.
* Includes the legacy Simple HTML DOM library to parse and extract desired content from HTML.  NOTE:  Simple HTML DOM is only included for legacy reasons.  TagFilter is much faster and more accurate as well as more powerful and flexible.
* DNS over HTTPS support.
* International domain name (IDNA/Punycode) support.
* An unncessarily [feature-laden web server class](https://github.com/cubiclesoft/ultimate-web-scraper/blob/master/docs/web_server.md) with optional SSL/TLS support.  Run a web server written in pure PHP.  Why?  Because you can, that's why.
* A decent [WebSocket server class](https://github.com/cubiclesoft/ultimate-web-scraper/blob/master/docs/websocket_server.md) is included too.  For a scalable version of the WebSocket server class, see [Data Relay Center](https://github.com/cubiclesoft/php-drc).
* Can be used to [download entire websites for offline use](#offline-downloading).
* Has a liberal open source license.  MIT or LGPL, your choice.
* Designed for relatively painless integration into your project.
* Sits on GitHub for all of that pull request and issue tracker goodness to easily submit changes and ideas respectively.

Getting Started
---------------

[![Web Scraping - Techniques and tools of the trade](https://user-images.githubusercontent.com/1432111/42725116-523907e6-8733-11e8-8322-71631f5e198a.png "Watch video")](https://www.youtube.com/watch?v=54tB8t1r0og)

Example object-oriented usage:

```php
<?php
	require_once "support/web_browser.php";
	require_once "support/tag_filter.php";

	// Retrieve the standard HTML parsing array for later use.
	$htmloptions = TagFilter::GetHTMLOptions();

	// Retrieve a URL (emulating Firefox by default).
	$url = "http://www.somesite.com/something/";
	$web = new WebBrowser();
	$result = $web->Process($url);

	// Check for connectivity and response errors.
	if (!$result["success"])
	{
		echo "Error retrieving URL.  " . $result["error"] . "\n";
		exit();
	}

	if ($result["response"]["code"] != 200)
	{
		echo "Error retrieving URL.  Server returned:  " . $result["response"]["code"] . " " . $result["response"]["meaning"] . "\n";
		exit();
	}

	// Get the final URL after redirects.
	$baseurl = $result["url"];

	// Use TagFilter to parse the content.
	$html = TagFilter::Explode($result["body"], $htmloptions);

	// Retrieve a pointer object to the root node.
	$root = $html->Get();

	// Find all anchor tags inside a div with a specific class.
	// A useful CSS selector cheat sheet:  https://gist.github.com/magicznyleszek/809a69dd05e1d5f12d01
	echo "All the URLs:\n";
	$rows = $root->Find("div.someclass a[href]");
	foreach ($rows as $row)
	{
		echo "\t" . $row->href . "\n";
		echo "\t" . HTTP::ConvertRelativeToAbsoluteURL($baseurl, $row->href) . "\n";
	}

	// Find all table rows that have 'th' tags.
	$rows = $root->Find("tr")->Filter("th");
	foreach ($rows as $row)
	{
		echo "\t" . $row->GetOuterHTML() . "\n\n";
	}

	// Find the OpenGraph URL in the meta tags of the HTML (if any).
	// For example:  <meta property="og:url" content="SOMEURL" />
	// The next line first finds all matching rows and then current() returns the first row.
	$metaurl = $root->Find("meta[property=\"og:url\"]")->current();
	if ($metaurl !== false)  echo trim($metaurl->content) . "\n\n";
?>
```

Example direct ID usage:

```php
<?php
	require_once "support/web_browser.php";
	require_once "support/tag_filter.php";

	// Retrieve the standard HTML parsing array for later use.
	$htmloptions = TagFilter::GetHTMLOptions();

	// Retrieve a URL (emulating Firefox by default).
	$url = "http://www.somesite.com/something/";
	$web = new WebBrowser();
	$result = $web->Process($url);

	// Check for connectivity and response errors.
	if (!$result["success"])
	{
		echo "Error retrieving URL.  " . $result["error"] . "\n";
		exit();
	}

	if ($result["response"]["code"] != 200)
	{
		echo "Error retrieving URL.  Server returned:  " . $result["response"]["code"] . " " . $result["response"]["meaning"] . "\n";
		exit();
	}

	// Get the final URL after redirects.
	$baseurl = $result["url"];

	// Use TagFilter to parse the content.
	$html = TagFilter::Explode($result["body"], $htmloptions);

	// Find all anchor tags inside a div with a specific class.
	// A useful CSS selector cheat sheet:  https://gist.github.com/magicznyleszek/809a69dd05e1d5f12d01
	echo "All the URLs:\n";
	$result2 = $html->Find("div.someclass a[href]");
	if (!$result2["success"])
	{
		echo "Error parsing/finding URLs.  " . $result2["error"] . "\n";
		exit();
	}

	foreach ($result2["ids"] as $id)
	{
		// Faster direct access.
		echo "\t" . $html->nodes[$id]["attrs"]["href"] . "\n";
		echo "\t" . HTTP::ConvertRelativeToAbsoluteURL($baseurl, $html->nodes[$id]["attrs"]["href"]) . "\n";
	}

	// Find all table rows that have 'th' tags.
	// The 'tr' tag IDs are returned.
	$result2 = $html->Filter($html->Find("tr"), "th");
	if (!$result2["success"])
	{
		echo "Error parsing/finding table rows.  " . $result2["error"] . "\n";
		exit();
	}

	foreach ($result2["ids"] as $id)
	{
		echo "\t" . $html->GetOuterHTML($id) . "\n\n";
	}
?>
```

Example HTML form extraction:

```php
<?php
	require_once "support/web_browser.php";
	require_once "support/tag_filter.php";

	// Retrieve the standard HTML parsing array for later use.
	$htmloptions = TagFilter::GetHTMLOptions();

	$url = "https://www.somewebsite.com/login/";

	// Turn on the automatic forms extraction option.  Note that Javascript is not executed.
	$web = new WebBrowser(array("extractforms" => true));
	$result = $web->Process($url);

	if (!$result["success"])
	{
		echo "Error retrieving URL.  " . $result["error"] . "\n";
		exit();
	}

	if ($result["response"]["code"] != 200)
	{
		echo "Error retrieving URL.  Server returned:  " . $result["response"]["code"] . " " . $result["response"]["meaning"] . "\n";
		exit();
	}

	if (count($result["forms"]) != 1)
	{
		echo "Was expecting one form.  Received:  " . count($result["forms"]) . "\n";
		exit();
	}

	// Forms are extracted in the order they appear in the HTML.
	$form = $result["forms"][0];

	// Set some or all of the variables in the form.
	$form->SetFormValue("username", "cooldude123");
	$form->SetFormValue("password", "password123");

	// Submit the form.
	$result2 = $form->GenerateFormRequest();
	$result = $web->Process($result2["url"], $result2["options"]);

	if (!$result["success"])
	{
		echo "Error retrieving URL.  " . $result["error"] . "\n";
		exit();
	}

	if ($result["response"]["code"] != 200)
	{
		echo "Error retrieving URL.  Server returned:  " . $result["response"]["code"] . " " . $result["response"]["meaning"] . "\n";
		exit();
	}

	// Use TagFilter to parse the content.
	$html = TagFilter::Explode($result["body"], $htmloptions);

	// Do something with the response here...
?>
```

Example POST request:

```php
<?php
	require_once "support/web_browser.php";

	$url = "https://api.somesite.com/profile";

	// Send a POST request to a URL.
	$web = new WebBrowser();
	$options = array(
		"postvars" => array(
			"id" => 12345,
			"firstname" => "John",
			"lastname" => "Smith"
		)
	);

	$result = $web->Process($url, $options);

	if (!$result["success"])
	{
		echo "Error retrieving URL.  " . $result["error"] . "\n";
		exit();
	}

	if ($result["response"]["code"] != 200)
	{
		echo "Error retrieving URL.  Server returned:  " . $result["response"]["code"] . " " . $result["response"]["meaning"] . "\n";
		exit();
	}

	// Do something with the response.
?>
```

Example large file/content retrieval:

```php
<?php
	require_once "support/web_browser.php";

	function DownloadFileCallback($response, $data, $opts)
	{
		if ($response["code"] == 200)
		{
			$size = ftell($opts);
			fwrite($opts, $data);

			if ($size % 1000000 > ($size + strlen($data)) % 1000000)  echo ".";
		}

		return true;
	}

	// Download a large file.
	$url = "http://downloads.somesite.com/large_file.zip";
	$fp = fopen("the_file.zip", "wb");
	$web = new WebBrowser();
	$options = array(
		"read_body_callback" => "DownloadFileCallback",
		"read_body_callback_opts" => $fp
	);
	echo "Downloading '" . $url . "'...";
	$result = $web->Process($url, $options);
	echo "\n";
	fclose($fp);

	// Check for connectivity and response errors.
	if (!$result["success"])
	{
		echo "Error retrieving URL.  " . $result["error"] . "\n";
		exit();
	}

	if ($result["response"]["code"] != 200)
	{
		echo "Error retrieving URL.  Server returned:  " . $result["response"]["code"] . " " . $result["response"]["meaning"] . "\n";
		exit();
	}

	// Do something with the response.
?>
```

Example custom SSL options usage:

```php
<?php
	require_once "support/http.php";
	require_once "support/web_browser.php";

	// Generate default safe SSL/TLS options using the "modern" ciphers.
	// See:  https://mozilla.github.io/server-side-tls/ssl-config-generator/
	$sslopts = HTTP::GetSafeSSLOpts(true, "modern");

	// Adjust the options as necessary.
	// For a complete list of options, see:  http://php.net/manual/en/context.ssl.php
	$sslopts["capture_peer_cert"] = true;

	// Demonstrates capturing the SSL certificate.
	// Returning false terminates the connection without sending any data.
	function CertCheckCallback($type, $cert, $opts)
	{
		var_dump($type);
		var_dump($cert);

		return true;
	}

	// Send a POST request to a URL.
	$url = "https://api.somesite.com/profile";
	$web = new WebBrowser();
	$options = array(
		"sslopts" => $sslopts,
		"peer_cert_callback" => "CertCheckCallback",
		"peer_cert_callback_opts" => false,
		"postvars" => array(
			"id" => 12345,
			"firstname" => "John",
			"lastname" => "Smith"
		)
	);
	$result = $web->Process($url, $options);

	// Check for connectivity and response errors.
	if (!$result["success"])
	{
		echo "Error retrieving URL.  " . $result["error"] . "\n";
		exit();
	}

	if ($result["response"]["code"] != 200)
	{
		echo "Error retrieving URL.  Server returned:  " . $result["response"]["code"] . " " . $result["response"]["meaning"] . "\n";
		exit();
	}

	// Do something with the response.
?>
```

Example debug mode usage:

```php
<?php
	require_once "support/web_browser.php";

	// Send a POST request to a URL with debugging enabled.
	// Enabling debug mode for a request uses more RAM since it collects all data sent and received over the wire.
	$url = "https://api.somesite.com/profile";
	$web = new WebBrowser();
	$options = array(
		"debug" => true,
		"postvars" => array(
			"id" => 12345,
			"firstname" => "John",
			"lastname" => "Smith"
		)
	);
	$result = $web->Process($url, $options);

	// Check for connectivity errors.
	if (!$result["success"])
	{
		echo "Error retrieving URL.  " . $result["error"] . "\n";
		exit();
	}

	echo "------- RAW SEND START -------\n";
	echo $result["rawsend"];
	echo "------- RAW SEND END -------\n\n";

	echo "------- RAW RECEIVE START -------\n";
	echo $result["rawrecv"];
	echo "------- RAW RECEIVE END -------\n\n";
?>
```

Uploading Files
---------------

File uploads are handled several different ways so that very large files can be processed.  The "files" option is an array of arrays that represents one or more files to upload.  File uploads will automatically switch a POST request's `Content-Type` from "application/x-www-form-urlencoded" to "multipart/form-data".

```php
<?php
	require_once "support/web_browser.php";

	// Upload two files.
	$url = "http://api.somesite.com/photos";
	$web = new WebBrowser();
	$options = array(
		"postvars" => array(
			"uid" => 12345
		),
		"files" => array(
			array(
				"name" => "file1",
				"filename" => "mycat.jpg",
				"type" => "image/jpeg",
				"data" => file_get_contents("/path/to/mycat.jpg")
			),
			array(
				"name" => "file2",
				"filename" => "mycat-hires.jpg",
				"type" => "image/jpeg",
				"datafile" => "/path/to/mycat-hires.jpg"
			)
		)
	);
	$result = $web->Process($url, $options);

	// Check for connectivity and response errors.
	if (!$result["success"])
	{
		echo "Error retrieving URL.  " . $result["error"] . "\n";
		exit();
	}

	if ($result["response"]["code"] != 200)
	{
		echo "Error retrieving URL.  Server returned:  " . $result["response"]["code"] . " " . $result["response"]["meaning"] . "\n";
		exit();
	}

	// Do something with the response.
?>
```

Each file in the "files" array must have the following options:

* name - The server-side key to use.
* filename - The filename to send to the server.  Well-written server-side software will generally ignore this other than to look at the file extension (e.g. ".jpg", ".png", ".pdf").
* type - The MIME type to send to the server.  Run a Google search for "mime type for xyz" where "xyz" is the file extension of the file you are sending.

One of the following options must also be provided for each file:

* data - A string containing the data to send.  This should only be used for small files.
* datafile - 
... [TRUNCATED]
```

### File: doh_web_browser.php
```php
<?php
	// CubicleSoft DNS over HTTPS web browser class.
	// (C) 2021 CubicleSoft.  All Rights Reserved.

	if (!class_exists("WebBrowser", false))  require_once str_replace("\\", "/", dirname(__FILE__)) . "/web_browser.php";

	// Requires the CubicleSoft WebBrowser class.
	class DOHWebBrowser extends WebBrowser
	{
		protected $dohapi, $dohhost, $dohtypes, $dohweb, $dohfp;
		protected static $dohcache;

		public function __construct($prevstate = array())
		{
			parent::__construct($prevstate);

			$this->SetDOHAccessInfo("https://cloudflare-dns.com/dns-query");

			if (!is_array(self::$dohcache))  self::$dohcache = array();
		}

		public function SetDOHAccessInfo($dohapi, $dohhost = false, $dohtypes = array("A", "AAAA"))
		{
			$this->dohapi = $dohapi;
			$this->dohhost = $dohhost;
			$this->dohtypes = $dohtypes;
			$this->dohweb = false;
			$this->dohfp = false;
		}

		public function ClearDOHCache()
		{
			self::$dohcache = array();
		}

		public function GetDOHCache()
		{
			return self::$dohcache;
		}

		// Override WebBrowser ProcessState().
		public function ProcessState(&$state)
		{
			if (!isset($state["tempoptions"]["doh_pre_retrievewebpage_callback"]))
			{
				$state["tempoptions"]["doh_pre_retrievewebpage_callback"] = (isset($state["tempoptions"]["pre_retrievewebpage_callback"]) && is_callable($state["tempoptions"]["pre_retrievewebpage_callback"]) ? $state["tempoptions"]["pre_retrievewebpage_callback"] : false);

				$state["tempoptions"]["pre_retrievewebpage_callback"] = array($this, "InternalDNSOverHTTPSHandler");
			}

			return parent::ProcessState($state);
		}

		public function InternalDNSOverHTTPSHandler(&$state)
		{
			// Skip hosts that appear to be IP addresses.
			$host = $state["urlinfo"]["host"];
			if (strpos($host, ":") === false && !preg_match('/^[0-9.]+$/', $host))
			{
				if (isset(self::$dohcache[$host]) && self::$dohcache[$host]["expires"] < time())  unset(self::$dohcache[$host]);

				// Obtain the IP address to connect to and cache it for later reuse.
				if (!isset(self::$dohcache[$host]))
				{
					if ($this->dohweb === false)  $this->dohweb = new WebBrowser();

					foreach ($this->dohtypes as $type)
					{
						$options = array(
							"headers" => array(
								"Accept" => "application/dns-json",
								"Connection" => "Keep-Alive"
							)
						);

						if ($this->dohhost !== false)  $options["headers"]["Host"] = $this->dohhost;
						if ($this->dohfp !== false)  $options["fp"] = $this->dohfp;

						$url2 = $this->dohapi . "?name=" . urlencode($host) . "&type=" . urlencode($type);

						$result = $this->dohweb->Process($url2, $options);
						if ($result["success"] && $result["response"]["code"] == 200)
						{
							if (isset($result["fp"]))  $this->dohfp = $result["fp"];

							$data = @json_decode($result["body"], true);
							if (is_array($data) && $data["Status"] == 0 && count($data["Answer"]))
							{
								self::$dohcache[$host] = $data["Answer"][0];
								self::$dohcache[$host]["expires"] = time() + self::$dohcache[$host]["TTL"];
								self::$dohcache[$host]["stype"] = $type;

								break;
							}
						}
					}
				}

				if (!isset(self::$dohcache[$host]))  return false;

				$state["options"]["headers"]["Host"] = $state["urlinfo"]["host"];
				$state["urlinfo"]["host"] = self::$dohcache[$host]["data"];
				$state["url"] = HTTP::CondenseURL($state["urlinfo"]);
			}

			if ($state["options"]["doh_pre_retrievewebpage_callback"] !== false && !call_user_func_array($state["options"]["doh_pre_retrievewebpage_callback"], array(&$state)))  return false;

			return true;
		}
	}
?>
```

### File: offline_download_example.php
```php
<?php
	// Basic website downloader.
	// (C) 2019 CubicleSoft.  All Rights Reserved.

	if (!isset($_SERVER["argc"]) || !$_SERVER["argc"])
	{
		echo "This file is intended to be run from the command-line.";

		exit();
	}

	// Temporary root.
	$rootpath = str_replace("\\", "/", dirname(__FILE__));

	require_once $rootpath . "/support/http.php";
	require_once $rootpath . "/support/web_browser.php";
	require_once $rootpath . "/support/tag_filter.php";
	require_once $rootpath . "/support/multi_async_helper.php";

	if ($argc < 3)
	{
		echo "Basic website downloader tool\n";
		echo "Purpose:  Download a website including HTML, image files, CSS, and directly referenced Javascript files.\n";
		echo "\n";
		echo "Syntax:  " . $argv[0] . " destdir starturl [linkdepth]\n";
		echo "\n";
		echo "Examples:\n";
		echo "\tphp " . $argv[0] . " offline-test https://barebonescms.com/ 3\n";

		exit();
	}

	// Don't let PHP run out of RAM.
	@ini_set("memory_limit", "-1");

	@mkdir($argv[1], 0770, true);
	$destpath = realpath($argv[1]);

	// Link traversal depth.
	$linkdepth = ($argc > 3 ? (int)$argv[3] : false);

	// Alter input URL to remove potential attack vectors.
	$initurl = $argv[2];
	$initurl2 = HTTP::ExtractURL($initurl);

	$initurl2["authority"] = strtolower($initurl2["authority"]);
	$initurl2["host"] = strtolower($initurl2["host"]);
	if ($initurl2["path"] === "")  $initurl2["path"] = "/";

	$initurl3 = $initurl2;
	$initurl3["host"] = "";
	$initurl2["path"] = "/";

	$initurl = HTTP::ConvertRelativeToAbsoluteURL($initurl2, $initurl3);

	$manifestfile = $destpath . "/" . str_replace(":", "_", $initurl2["authority"]) . "_manifest.json";
	$opsfile = $destpath . "/" . str_replace(":", "_", $initurl2["authority"]) . "_ops_" . md5(($linkdepth === false ? "-1" : $linkdepth) . "|" . $initurl) . ".json";

	$destpath .= "/" . str_replace(":", "_", $initurl2["authority"]);
	@mkdir($destpath, 0770, true);

	$helper = new MultiAsyncHelper();
	$helper->SetConcurrencyLimit(4);

	$htmloptions = TagFilter::GetHTMLOptions();
	$htmloptions["keep_comments"] = true;

	// Provides some basic feedback prior to retrieving each URL.
	function DisplayURL(&$state)
	{
		global $ops;

		echo "[" . number_format(count($ops), 0) . " ops] Retrieving '" . $state["url"] . "'...\n";

		return true;
	}

	// Calculates the static file extension based on the result of a HTTP request.
	function GetResultFileExtension(&$result)
	{
		$mimeextmap = array(
			"text/html" => ".html",
			"text/plain" => ".txt",
			"image/jpeg" => ".jpg",
			"image/png" => ".png",
			"image/gif" => ".gif",
			"text/css" => ".css",
			"text/javascript" => ".js",
		);

		// Attempt to map a Content-Type header to a file extension.
		if (isset($result["headers"]["Content-Type"]))
		{
			$header = HTTP::ExtractHeader($result["headers"]["Content-Type"][0]);

			if (isset($mimeextmap[strtolower($header[""])]))  return $mimeextmap[$header[""]];
		}

		$fileext = false;

		// Attempt to map a Content-Disposition header to a file extension.
		if (isset($result["headers"]["Content-Disposition"]))
		{
			$header = HTTP::ExtractHeader($result["headers"]["Content-Type"][0]);

			if ($header[""] === "attachment" && isset($header["filename"]))
			{
				$filename = explode("/", str_replace("\\", "/", $header["filename"]));
				$filename = array_pop($filename);
				$pos = strrpos($filename, ".");
				if ($pos !== false)  $fileext = strtolower(substr($filename, $pos));
			}
		}

		// Parse the URL and attempt to map to a file extension.
		if ($fileext === false)
		{
			$url = HTTP::ExtractURL($result["url"]);

			$filename = explode("/", str_replace("\\", "/", $url["path"]));
			$filename = array_pop($filename);
			$pos = strrpos($filename, ".");
			if ($pos !== false)  $fileext = strtolower(substr($filename, $pos));
		}

		if ($fileext === false)  $fileext = ".html";

		// Avoid unfortunate/accidental local code execution via a localhost web server.
		$maptohtml = array(
			".php" => true,
			".php3" => true,
			".php4" => true,
			".php5" => true,
			".php7" => true,
			".phtml" => true,
			".asp" => true,
			".aspx" => true,
			".cfm" => true,
			".jsp" => true,
			".pl" => true,
			".cgi" => true,
		);

		if (isset($maptohtml[$fileext]))  $fileext = ".html";

		return $fileext;
	}

	// Attempt to create a roughly-equivalent structure to the URL on the local filesystem for static serving later.
	function SetReverseManifestPath($key)
	{
		global $ops, $opsdata, $initurl2, $manifestrev, $destpath;

		$url2 = HTTP::ExtractURL($key);
		$path = "";
		if (strcasecmp($url2["authority"], $initurl2["authority"]) != 0)  $path .= "/" . str_replace(":", "_", strtolower($url2["authority"]));
		$path .= ($url2["path"] !== "" ? $url2["path"] : "/");
		$path = explode("/", str_replace("\\", "/", TagFilterStream::MakeValidUTF8($path)));
		$filename = array_pop($path);
		if ($filename === "")  $filename = "index";

		$pos = strrpos($filename, ".");
		if ($pos !== false)  $filename = substr($filename, 0, $pos);

		if ($url2["query"] !== "")  $filename .= "_" . md5($url2["query"]);

		// Make a clean directory.
		$vals = $path;
		$path = array_shift($vals) . "/";
		while (count($vals))
		{
			$path .= array_shift($vals);

			if (isset($manifestrev[strtolower($path)]))  $path = $manifestrev[strtolower($path)];
			else  $manifestrev[strtolower($path)] = $path;

			$x = 0;
			while (is_file($destpath . $path . ($x ? "_" . ($x + 1) : "")))  $x++;

			if ($x)  $path .= "_" . ($x + 1);

			$path .= "/";
		}

		@mkdir($destpath . $path, 0770, true);

		// And a clean filename.
		$path .= $filename;

		$x = 0;
		while (isset($manifestrev[strtolower($path . ($x ? "_" . ($x + 1) : "") . $ops[$key]["ext"])]) || is_dir($path . ($x ? "_" . ($x + 1) : "") . $ops[$key]["ext"]))  $x++;

		$path .= ($x ? "_" . ($x + 1) : "") . $ops[$key]["ext"];

		$opsdata[$key]["path"] = $path;

		// Reserve an entry in the reverse manifest for the full path/filename.
		$manifestrev[strtolower($path)] = $path;

//var_dump($opsdata[$key]["path"]);
//var_dump($manifestrev);
	}

	// Maps a manifest item to a static path on disk.
	$processedurls = array();
	function MapManifestResourceItem($parenturl, $url)
	{
		global $manifest, $processedurls, $opsdata;

		// Strip scheme if HTTP/HTTPS.  Otherwise, just return the URL as-is (e.g. mailto: and data: URIs).
		if (strtolower(substr($url, 0, 7)) === "http://")  $url2 = substr($url, 5);
		else if (strtolower(substr($url, 0, 8)) === "https://")  $url2 = substr($url, 6);
		else  return $url;

		// If already processed and valid, return the relative reference to the path on disk.
		if ($parenturl !== false && isset($opsdata[$parenturl]) && (isset($manifest[$url2]) || isset($opsdata[$url])))
		{
			$path = explode("/", $opsdata[$parenturl]["path"]);
			$path2 = explode("/", (isset($manifest[$url2]) ? $manifest[$url2] : $opsdata[$url]["path"]));

			array_pop($path);

			while (count($path) && count($path2) && $path[0] === $path2[0])
			{
				array_shift($path);
				array_shift($path2);
			}

			$path2 = str_repeat("../", count($path)) . implode("/", $path2);

			return $path2;
		}

		// If already processed but not valid (e.g. a 404 error), just return the URL.
		if (isset($processedurls[$url]))  return $url;

		return false;
	}

	// Generates a leaf node and prevents the parent from completing until the document URLs are updated.
	function PrepareManifestResourceItem($parenturl, $forcedext, $url)
	{
		global $ops, $helper;

		$pos = strpos($url, "#");
		if ($pos === false)  $fragment = false;
		else
		{
			$fragment = substr($url, $pos);
			$url = substr($url, 0, $pos);
		}

		// Skip downloading if the item has already been processed.
		$url2 = MapManifestResourceItem($parenturl, $url);
		if ($url2 !== false)  return $url2 . $fragment;

		// Queue the resource request.
		$key = $url;

		if (!isset($ops[$key]))
		{
			$ops[$key] = array(
				"type" => "res",
				"status" => "download",
				"depth" => 0,
				"retries" => 3,
				"ext" => $forcedext,
				"waiting" => array(),
				"web" => ($parenturl === false ? new WebBrowser(array("followlocation" => false)) : clone $ops[$parenturl]["web"]),
				"options" => array(
					"pre_retrievewebpage_callback" => "DisplayURL"
				)
			);

			$ops[$key]["web"]->ProcessAsync($helper, $key, NULL, $url, $ops[$key]["options"]);
		}

		// Set the waiting status for the parent.
		if ($parenturl !== false)
		{
			if ($ops[$parenturl]["status"] === "waiting")  $ops[$parenturl]["wait_refs"]++;
			else
			{
				$ops[$parenturl]["status"] = "waiting";
				$ops[$parenturl]["wait_refs"] = 1;
			}

			$ops[$key]["waiting"][] = $parenturl;
		}

		return $url;
	}

	// Locate additional files to import in CSS.  Doesn't implement a state engine.
	function ProcessCSS($css, $parenturl, $baseurl)
	{
		$result = $css;

		// Strip comments.
		$css = str_replace("<" . "!--", " ", $css);
		$css = str_replace("--" . ">", " ", $css);
		while (($pos = strpos($css, "/*")) !== false)
		{
			$pos2 = strpos($css, "*/", $pos + 2);
			if ($pos2 === false)  $pos2 = strlen($css);
			else  $pos2 += 2;

			$css = substr($css, 0, $pos) . substr($css, $pos2);
		}

		// Alter @import lines.
		$pos = 0;
		while (($pos = stripos($css, "@import", $pos)) !== false)
		{
			$semipos = strpos($css, ";", $pos);
			if ($semipos === false)  break;

			$pos2 = strpos($css, "'", $pos);
			if ($pos2 === false)  $pos2 = strpos($css, "\"", $pos);
			if ($pos2 === false)  break;

			$pos3 = strpos($css, $css[$pos2], $pos2 + 1);
			if ($pos3 === false)  break;

			if ($pos2 < $semipos && $pos3 < $semipos)
			{
				$url = HTTP::ConvertRelativeToAbsoluteURL($baseurl, substr($css, $pos2 + 1, $pos3 - $pos2 - 1));

				$result = str_replace(substr($css, $pos2, $pos3 - $pos2 + 1), $css[$pos2] . PrepareManifestResourceItem($parenturl, ".css", $url) . $css[$pos2], $result);
			}

			$pos = $semipos + 1;
		}

		// Alter url() values.
		$pos = 0;
		while (($pos = stripos($css, "url(", $pos)) !== false)
		{
			$endpos = strpos($css, ")", $pos);
			if ($endpos === false)  break;

			$pos2 = strpos($css, "'", $pos);
			if ($pos2 !== false && $pos2 > $endpos)  $pos2 = false;
			if ($pos2 === false)  $pos2 = strpos($css, "\"", $pos);

			if ($pos2 === false || $pos2 > $endpos)
			{
				$pos2 = $pos + 3;
				$pos3 = $endpos;
			}
			else
			{
				$pos3 = strpos($css, $css[$pos2], $pos2 + 1);
				if ($pos3 === false || $pos3 > $endpos)  $pos3 = $endpos;
			}

			$url = HTTP::ConvertRelativeToAbsoluteURL($baseurl, substr($css, $pos2 + 1, $pos3 - $pos2 - 1));

			$result = str_replace(substr($css, $pos2, $pos3 - $pos2 + 1), $css[$pos2] . PrepareManifestResourceItem($parenturl, false, $url) . $css[$pos3], $result);

			$pos = $endpos + 1;
		}

		return $result;
	}

	function ProcessContent($key, $final)
	{
		global $ops, $opsdata, $htmloptions, $initurl2, $linkdepth, $helper;

		// Process HTML, altering URLs as necessary.
		if ($ops[$key]["type"] === "node" && $ops[$key]["ext"] === ".html")
		{
			$html = TagFilter::Explode($opsdata[$key]["content"], $htmloptions);
			$root = $html->Get();

			$urlinfo = HTTP::ExtractURL($opsdata[$key]["url"]);

			// Handle images.
			$rows = $root->Find('img[src],img[srcset],picture source[srcset]');
			foreach ($rows as $row)
			{
				if (isset($row->src))
				{
					$url = HTTP::ConvertRelativeToAbsoluteURL($urlinfo, $row->src);

					$row->src = PrepareManifestResourceItem($key, false, $url);
				}

				if (isset($row->srcset))
				{
					$urls = explode(",", $row->srcset);
					$urls2 = array();
					foreach ($urls as $url)
					{
						$url = trim($url);
						$pos = strrpos($url, " ");
						if ($pos !== false)
						{
							$url2 = HTTP::ConvertRelativeToAbsoluteURL($urlinfo, trim(substr($url, 0, $pos)));
							$size = substr($url, $pos + 1);

							$urls2[] = PrepareManifestResourceItem($key, false, $url2) . " " . $size;
						}
					}

					$row->srcset = implode(", ", $urls2);
				}
			}

			// Handle link tags with hrefs.
			$rows = $root->Find('link[href],use[xlink\:href]');
			foreach ($rows as $row)
			{
				$url = HTTP::ConvertRelativeToAbsoluteURL($urlinfo, (isset($row->href) ? $row->href : $row->{"xlink:href"}));

				$row->href = PrepareManifestResourceItem($key, ((isset($row->rel) && strtolower($row->rel) === "stylesheet") || (isset($row->type) && strtolower($row->type) === "text/css") ? ".css" : false), $url);
			}

			// Handle external Javascript.
			$rows = $root->Find('script[src]');
			foreach ($rows as $row)
			{
				$url = HTTP::ConvertRelativeToAbsoluteURL($urlinfo, $row->src);

				$row->src = PrepareManifestResourceItem($key, ".js", $url);
			}

			// Handle style tags.
			$rows = $root->Find('style');
			foreach ($rows as $row)
			{
				$children = $row->Children(true);
				foreach ($children as $child)
				{
					if ($child->Type() === "content")
					{
						$child->Text(ProcessCSS($child->Text(), $key, $urlinfo));
					}
				}
			}

			// Handle inline styles.
			$rows = $root->Find('[style]');
			foreach ($rows as $row)
			{
				$row->style = ProcessCSS($row->style, $key, $urlinfo);
			}

			// Handle anchor tags and iframes.
			$rows = $root->Find('a[href],iframe[src]');
			foreach ($rows as $row)
			{
				$url = ($row->Tag() === "iframe" ? $row->src : $row->href);

				// Skip altering fragment-only URIs.  The browser knows how to natively handle these.
				if (substr($url, 0, 1) === "#")  continue;

				$url = HTTP::ConvertRelativeToAbsoluteURL($urlinfo, $url);
				$url2 = HTTP::ExtractURL($url);

				// Only follow links on the same domain.
				if (strcasecmp($url2["authority"], $initurl2["authority"]) == 0 && ($url2["scheme"] === "http" || $url2["scheme"] === "https"))
				{
					if ($url2["path"] === "")
					{
						$url2["path"] = "/";
						$url = HTTP::CondenseURL($url2);
					}

					$pos = strpos($url, "#");
					if ($pos === false)  $fragment = false;
					else
					{
						$fragment = substr($url, $pos);
						$url = substr($url, 0, $pos);
					}

					$url2 = MapManifestResourceItem($key, $url);
					if ($url2 !== false)
					{
						if ($row->Tag() === "iframe")  $row->src = $url2 . $fragment;
						else  $row->href = $url2 . $fragment;
					}
					else
					{
						if ($row->Tag() === "iframe")  $row->src = $url . $fragment;
						else  $row->href = $url . $fragment;

						if ($linkdepth === false || $ops[$key]["depth"] < $linkdepth)
						{
							// Queue up another node.
							$key2 = $url;

							if (!isset($ops[$key2]))
							{
								$ops[$key2] = array(
									"type" => "node",
									"status" => "download",
									"depth" => $ops[$key]["depth"] + 1,
									"retries" => 3,
									"ext" => false,
									"waiting" => array(),
									"web" => clone $ops[$key]["web"],
									"options" => array(
										"pre_retrievewebpage_callback" => "DisplayURL"
									)
								);

								$ops[$key]["web"]->ProcessAsync($helper, $key2, NULL, $url, $ops[$key2]["options"]);
							}

							if ($key !== $key2)
							{
								if ($ops[$key]["statu
... [TRUNCATED]
```

### File: websocket_server.php
```php
<?php
	// CubicleSoft PHP WebSocketServer class.
	// (C) 2021 CubicleSoft.  All Rights Reserved.

	// Make sure PHP doesn't introduce weird limitations.
	ini_set("memory_limit", "-1");
	set_time_limit(0);

	// Requires the CubicleSoft PHP WebSocket class.
	class WebSocketServer
	{
		protected $fp, $clients, $nextclientid, $websocketclass, $origins;
		protected $defaultclosemode, $defaultmaxreadframesize, $defaultmaxreadmessagesize, $defaultkeepalive, $lasttimeoutcheck;

		public function __construct()
		{
			$this->Reset();
		}

		public function Reset()
		{
			if (!class_exists("WebSocket", false))  require_once str_replace("\\", "/", dirname(__FILE__)) . "/websocket.php";

			$this->fp = false;
			$this->clients = array();
			$this->nextclientid = 1;
			$this->websocketclass = "WebSocket";
			$this->origins = false;

			$this->defaultclosemode = WebSocket::CLOSE_IMMEDIATELY;
			$this->defaultmaxreadframesize = 2000000;
			$this->defaultmaxreadmessagesize = 10000000;
			$this->defaultkeepalive = 30;
			$this->lasttimeoutcheck = time();
		}

		public function __destruct()
		{
			$this->Stop();
		}

		public function SetWebSocketClass($newclass)
		{
			if (class_exists($newclass))  $this->websocketclass = $newclass;
		}

		public function SetAllowedOrigins($origins)
		{
			if (is_string($origins))  $origins = array($origins);
			if (!is_array($origins))  $origins = false;
			else if (isset($origins[0]))  $origins = array_flip($origins);

			$this->origins = $origins;
		}

		public function SetDefaultCloseMode($mode)
		{
			$this->defaultclosemode = $mode;
		}

		public function SetDefaultKeepAliveTimeout($keepalive)
		{
			$this->defaultkeepalive = (int)$keepalive;
		}

		public function SetDefaultMaxReadFrameSize($maxsize)
		{
			$this->defaultmaxreadframesize = (is_bool($maxsize) ? false : (int)$maxsize);
		}

		public function SetDefaultMaxReadMessageSize($maxsize)
		{
			$this->defaultmaxreadmessagesize = (is_bool($maxsize) ? false : (int)$maxsize);
		}

		// Starts the server on the host and port.
		// $host is usually 0.0.0.0 or 127.0.0.1 for IPv4 and [::0] or [::1] for IPv6.
		public function Start($host, $port)
		{
			$this->Stop();

			$this->fp = stream_socket_server("tcp://" . $host . ":" . $port, $errornum, $errorstr);
			if ($this->fp === false)  return array("success" => false, "error" => self::WSTranslate("Bind() failed.  Reason:  %s (%d)", $errorstr, $errornum), "errorcode" => "bind_failed");

			// Enable non-blocking mode.
			stream_set_blocking($this->fp, 0);

			return array("success" => true);
		}

		public function Stop()
		{
			foreach ($this->clients as $client)
			{
				if ($client->websocket !== false)  $client->websocket->Disconnect();
				else  fclose($client->fp);
			}

			$this->clients = array();

			if ($this->fp !== false)
			{
				fclose($this->fp);

				$this->fp = false;
			}

			$this->nextclientid = 1;
		}

		// Dangerous but allows for stream_select() calls on multiple, separate stream handles.
		public function GetStream()
		{
			return $this->fp;
		}

		// Return whatever response/headers are needed here.
		protected function ProcessNewConnection($method, $path, $client)
		{
			$result = "";

			if ($method !== "GET")  $result .= "HTTP/1.1 405 Method Not Allowed\r\nConnection: close\r\n\r\n";
			else if (!isset($client->headers["Host"]) || !isset($client->headers["Connection"]) || stripos($client->headers["Connection"], "upgrade") === false || !isset($client->headers["Upgrade"]) || stripos($client->headers["Upgrade"], "websocket") === false || !isset($client->headers["Sec-Websocket-Key"]))
			{
				$result .= "HTTP/1.1 400 Bad Request\r\nConnection: close\r\n\r\n";
			}
			else if (!isset($client->headers["Sec-Websocket-Version"]) || $client->headers["Sec-Websocket-Version"] != 13)
			{
				$result .= "HTTP/1.1 426 Upgrade Required\r\nSec-WebSocket-Version: 13\r\nConnection: close\r\n\r\n";
			}
			else if (!isset($client->headers["Origin"]) || ($this->origins !== false && !isset($this->origins[strtolower($client->headers["Origin"])])))
			{
				$result .= "HTTP/1.1 403 Forbidden\r\nConnection: close\r\n\r\n";
			}

			return $result;
		}

		// Return whatever additional HTTP headers are needed here.
		protected function ProcessAcceptedConnection($method, $path, $client)
		{
			return "";
		}

		protected function InitNewClient($fp)
		{
			$client = new stdClass();

			$client->id = $this->nextclientid;
			$client->readdata = "";
			$client->writedata = "";
			$client->request = false;
			$client->path = "";
			$client->url = "";
			$client->headers = array();
			$client->lastheader = "";
			$client->websocket = false;
			$client->fp = $fp;
			$client->ipaddr = stream_socket_get_name($fp, true);

			// Intended for application storage.
			$client->appdata = false;

			$this->clients[$this->nextclientid] = $client;

			$this->nextclientid++;

			return $client;
		}

		private function ProcessInitialResponse($method, $path, $client)
		{
			// Let a derived class handle the new connection (e.g. processing Origin and Host).
			// Since the 'websocketclass' is instantiated AFTER this function, it is possible to switch classes on the fly.
			$client->writedata .= $this->ProcessNewConnection($method, $path, $client);

			// If an error occurs, the connection will still terminate.
			$client->websocket = new $this->websocketclass();
			$client->websocket->SetCloseMode($this->defaultclosemode);
			$client->websocket->SetKeepAliveTimeout($this->defaultkeepalive);

			// If nothing was output, accept the connection.
			if ($client->writedata === "")
			{
				$client->writedata .= "HTTP/1.1 101 Switching Protocols\r\nUpgrade: websocket\r\nConnection: Upgrade\r\n";
				$client->writedata .= "Sec-WebSocket-Accept: " . base64_encode(sha1($client->headers["Sec-Websocket-Key"] . WebSocket::KEY_GUID, true)) . "\r\n";
				$client->writedata .= $this->ProcessAcceptedConnection($method, $path, $client);
				$client->writedata .= "\r\n";

				// Finish class initialization.
				$client->websocket->SetServerMode();
				$client->websocket->SetMaxReadFrameSize($this->defaultmaxreadframesize);
				$client->websocket->SetMaxReadMessageSize($this->defaultmaxreadmessagesize);

				// Set the socket in the WebSocket class.
				$client->websocket->Connect("", "", array("connected_fp" => $client->fp));
			}

			$this->UpdateClientState($client->id);
		}

		public function UpdateStreamsAndTimeout($prefix, &$timeout, &$readfps, &$writefps)
		{
			if ($this->fp !== false)  $readfps[$prefix . "ws_s"] = $this->fp;
			if ($timeout === false || $timeout > $this->defaultkeepalive)  $timeout = $this->defaultkeepalive;

			foreach ($this->clients as $id => $client)
			{
				if ($client->writedata === "")  $readfps[$prefix . "ws_c_" . $id] = $client->fp;

				if ($client->writedata !== "" || ($client->websocket !== false && $client->websocket->NeedsWrite()))  $writefps[$prefix . "ws_c_" . $id] = $client->fp;

				if ($client->websocket !== false)
				{
					$timeout2 = $client->websocket->GetKeepAliveTimeout();
					if ($timeout > $timeout2)  $timeout = $timeout2;
				}
			}
		}

		// Sometimes keyed arrays don't work properly.
		public static function FixedStreamSelect(&$readfps, &$writefps, &$exceptfps, $timeout)
		{
			// In order to correctly detect bad outputs, no '0' integer key is allowed.
			if (isset($readfps[0]) || isset($writefps[0]) || ($exceptfps !== NULL && isset($exceptfps[0])))  return false;

			$origreadfps = $readfps;
			$origwritefps = $writefps;
			$origexceptfps = $exceptfps;

			$result2 = @stream_select($readfps, $writefps, $exceptfps, $timeout);
			if ($result2 === false)  return false;

			if (isset($readfps[0]))
			{
				$fps = array();
				foreach ($origreadfps as $key => $fp)  $fps[(int)$fp] = $key;

				foreach ($readfps as $num => $fp)
				{
					$readfps[$fps[(int)$fp]] = $fp;

					unset($readfps[$num]);
				}
			}

			if (isset($writefps[0]))
			{
				$fps = array();
				foreach ($origwritefps as $key => $fp)  $fps[(int)$fp] = $key;

				foreach ($writefps as $num => $fp)
				{
					$writefps[$fps[(int)$fp]] = $fp;

					unset($writefps[$num]);
				}
			}

			if ($exceptfps !== NULL && isset($exceptfps[0]))
			{
				$fps = array();
				foreach ($origexceptfps as $key => $fp)  $fps[(int)$fp] = $key;

				foreach ($exceptfps as $num => $fp)
				{
					$exceptfps[$fps[(int)$fp]] = $fp;

					unset($exceptfps[$num]);
				}
			}

			return true;
		}

		// Handles new connections, the initial conversation, basic packet management, and timeouts.
		// Can wait on more streams than just sockets and/or more sockets.  Useful for waiting on other resources.
		// 'ws_s' and the 'ws_c_' prefix are reserved.
		// Returns an array of clients that may need more processing.
		public function Wait($timeout = false, $readfps = array(), $writefps = array(), $exceptfps = NULL)
		{
			$this->UpdateStreamsAndTimeout("", $timeout, $readfps, $writefps);

			$result = array("success" => true, "clients" => array(), "removed" => array(), "readfps" => array(), "writefps" => array(), "exceptfps" => array(), "accepted" => array(), "read" => array(), "write" => array());
			if (!count($readfps) && !count($writefps))  return $result;

			$result2 = self::FixedStreamSelect($readfps, $writefps, $exceptfps, $timeout);
			if ($result2 === false)  return array("success" => false, "error" => self::WSTranslate("Wait() failed due to stream_select() failure.  Most likely cause:  Connection failure."), "errorcode" => "stream_select_failed");

			// Return handles that were being waited on.
			$result["readfps"] = $readfps;
			$result["writefps"] = $writefps;
			$result["exceptfps"] = $exceptfps;

			$this->ProcessWaitResult($result);

			return $result;
		}

		protected function ProcessWaitResult(&$result)
		{
			// Handle new connections.
			if (isset($result["readfps"]["ws_s"]))
			{
				while (($fp = @stream_socket_accept($this->fp, 0)) !== false)
				{
					// Enable non-blocking mode.
					stream_set_blocking($fp, 0);

					$client = $this->InitNewClient($fp);

					$result["accepted"][$client->id] = $client;
				}

				unset($result["readfps"]["ws_s"]);
			}

			// Handle clients in the read queue.
			foreach ($result["readfps"] as $cid => $fp)
			{
				if (!is_string($cid) || strlen($cid) < 6 || substr($cid, 0, 5) !== "ws_c_")  continue;

				$id = (int)substr($cid, 5);

				if (!isset($this->clients[$id]))  continue;

				$client = $this->clients[$id];

				$result["read"][$id] = $client;

				if ($client->websocket !== false)
				{
					$this->ProcessClientQueuesAndTimeoutState($result, $id, true, isset($result["writefps"][$cid]));

					// Remove active WebSocket clients from the write queue.
					unset($result["writefps"][$cid]);
				}
				else
				{
					$result2 = @fread($fp, 8192);
					if ($result2 === false || ($result2 === "" && feof($fp)))
					{
						@fclose($fp);

						unset($this->clients[$id]);
					}
					else
					{
						$client->readdata .= $result2;

						if (strlen($client->readdata) > 100000)
						{
							// Bad header size.  Just kill the connection.
							@fclose($fp);

							unset($this->clients[$id]);
						}
						else
						{
							while (($pos = strpos($client->readdata, "\n")) !== false)
							{
								// Retrieve the next line of input.
								$line = rtrim(substr($client->readdata, 0, $pos));
								$client->readdata = (string)substr($client->readdata, $pos + 1);

								if ($client->request === false)  $client->request = trim($line);
								else if ($line !== "")
								{
									// Process the header.
									if ($client->lastheader != "" && (substr($line, 0, 1) == " " || substr($line, 0, 1) == "\t"))  $client->headers[$client->lastheader] .= $header;
									else
									{
										$pos = strpos($line, ":");
										if ($pos === false)  $pos = strlen($line);
										$client->lastheader = self::HeaderNameCleanup(substr($line, 0, $pos));
										$client->headers[$client->lastheader] = ltrim(substr($line, $pos + 1));
									}
								}
								else
								{
									// Headers have all been received.  Process the client request.
									$request = $client->request;
									$pos = strpos($request, " ");
									if ($pos === false)  $pos = strlen($request);
									$method = (string)substr($request, 0, $pos);
									$request = trim(substr($request, $pos));

									$pos = strrpos($request, " ");
									if ($pos === false)  $pos = strlen($request);
									$path = (string)substr($request, 0, $pos);
									if ($path === "")  $path = "/";

									if (isset($client->headers["Host"]))  $client->headers["Host"] = preg_replace('/[^a-z0-9.:\[\]_-]/', "", strtolower($client->headers["Host"]));

									$client->path = $path;
									$client->url = "ws://" . (isset($client->headers["Host"]) ? $client->headers["Host"] : "localhost") . $path;

									$this->ProcessInitialResponse($method, $path, $client);

									break;
								}
							}
						}
					}
				}

				unset($result["readfps"][$cid]);
			}

			// Handle remaining clients in the write queue.
			foreach ($result["writefps"] as $cid => $fp)
			{
				if (!is_string($cid) || strlen($cid) < 6 || substr($cid, 0, 5) !== "ws_c_")  continue;

				$id = (int)substr($cid, 5);

				if (!isset($this->clients[$id]))  continue;

				$client = $this->clients[$id];

				$result["write"][$id] = $client;

				if ($client->writedata === "")  $this->ProcessClientQueuesAndTimeoutState($result, $id, false, true);
				else
				{
					$result2 = @fwrite($fp, $client->writedata);
					if ($result2 === false || ($result2 === "" && feof($fp)))
					{
						@fclose($fp);

						unset($this->clients[$id]);
					}
					else if ($result2 === 0)  $this->ProcessClientQueuesAndTimeoutState($result, $id, true, false, 1);
					else
					{
						$client->writedata = (string)substr($client->writedata, $result2);

						// Let the application know about the new client or close the connection if the WebSocket Upgrade request failed.
						if ($client->writedata === "")
						{
							if ($client->websocket->GetStream() !== false)  $result["clients"][$id] = $client;
							else
							{
								@fclose($fp);

								unset($this->clients[$id]);
							}
						}
					}
				}

				unset($result["writefps"][$cid]);
			}

			// Handle client timeouts.
			$ts = time();
			if ($this->lasttimeoutcheck <= $ts - 5)
			{
				foreach ($this->clients as $id => $client)
				{
					if (!isset($result["clients"][$id]) && $client->writedata === "" && $client->websocket !== false)
					{
						$this->ProcessClientQueuesAndTimeoutState($result, $id, false, false);
					}
				}

				$this->lasttimeoutcheck = $ts;
			}
		}

		protected function ProcessClientQueuesAndTimeoutState(&$result, $id, $read, $write, $readsize = 65536)
		{
			$client = $this->clients[$id];

			$result2 = $client->websocket->ProcessQueuesAndTimeoutState($read, $write, $readsize);
			if ($result2["success"])  $result["clients"][$id] = $client;
			else
			{
				$result["removed"]
... [TRUNCATED]
```

### File: websocket_server_libev.php
```php
<?php
	// CubicleSoft PHP WebSocketServer class with libev support.
	// (C) 2021 CubicleSoft.  All Rights Reserved.

	if (!class_exists("WebSocketServer", false))  require_once str_replace("\\", "/", dirname(__FILE__)) . "/websocket_server.php";

	class LibEvWebSocketServer extends WebSocketServer
	{
		protected $ev_watchers, $ev_read_ready, $ev_write_ready;

		public static function IsSupported()
		{
			$os = php_uname("s");
			$windows = (strtoupper(substr($os, 0, 3)) == "WIN");

			return (extension_loaded("ev") && !$windows);
		}

		public function Reset()
		{
			parent::Reset();

			$this->ev_watchers = array();
		}

		public function Internal_LibEvHandleEvent($watcher, $revents)
		{
			if (($revents & Ev::READ) || ($revents & Ev::ERROR))  $this->ev_read_ready[$watcher->data] = $watcher->fd;
			if ($revents & Ev::WRITE)  $this->ev_write_ready[$watcher->data] = $watcher->fd;
		}

		public function Start($host, $port)
		{
			$result = parent::Start($host, $port);
			if (!$result["success"])  return $result;

			$this->ev_watchers["ws_s"] = new EvIo($this->fp, Ev::READ, array($this, "Internal_LibEvHandleEvent"), "ws_s");

			return $result;
		}

		public function Stop()
		{
			parent::Stop();

			foreach ($this->ev_watchers as $key => $watcher)
			{
				$watcher->stop();
			}

			$this->ev_watchers = array();
		}

		protected function InitNewClient($fp)
		{
			$client = parent::InitNewClient($fp);

			$this->ev_watchers["ws_c_" . $client->id] = new EvIo($client->fp, Ev::READ, array($this, "Internal_LibEvHandleEvent"), "ws_c_" . $client->id);

			return $client;
		}

		public function UpdateStreamsAndTimeout($prefix, &$timeout, &$readfps, &$writefps)
		{
			if ($this->fp !== false)  $readfps[$prefix . "ws_s"] = $this->fp;
			if ($timeout === false || $timeout > $this->defaultkeepalive)  $timeout = $this->defaultkeepalive;

			foreach ($this->clients as $id => $client)
			{
				if ($client->writedata === "")  $readfps[$prefix . "ws_c_" . $id] = $client->fp;

				if ($client->writedata !== "" || ($client->websocket !== false && $client->websocket->NeedsWrite()))  $writefps[$prefix . "ws_c_" . $id] = $client->fp;
			}
		}

		public function Internal_LibEvTimeout($watcher, $revents)
		{
			Ev::stop(Ev::BREAK_ALL);
		}

		public function Wait($timeout = false, $readfps = array(), $writefps = array(), $exceptfps = NULL)
		{
			if ($timeout === false || $timeout > $this->defaultkeepalive)  $timeout = $this->defaultkeepalive;

			$result = array("success" => true, "clients" => array(), "removed" => array(), "readfps" => array(), "writefps" => array(), "exceptfps" => array(), "accepted" => array(), "read" => array(), "write" => array());
			if (!count($this->ev_watchers) && !count($readfps) && !count($writefps))  return $result;

			$this->ev_read_ready = array();
			$this->ev_write_ready = array();

			// Temporarily attach other read/write handles.
			$tempwatchers = array();

			foreach ($readfps as $key => $fp)
			{
				$tempwatchers[] = new EvIo($fp, Ev::READ, array($this, "Internal_LibEvHandleEvent"), $key);
			}

			foreach ($writefps as $key => $fp)
			{
				$tempwatchers[] = new EvIo($fp, Ev::WRITE, array($this, "Internal_LibEvHandleEvent"), $key);
			}

			$tempwatchers[] = new EvTimer($timeout, 0, array($this, "Internal_LibEvTimeout"));

			// Wait for one or more events to fire.
			Ev::run(Ev::RUN_ONCE);

			// Remove temporary watchers.
			foreach ($tempwatchers as $watcher)  $watcher->stop();

			// Return handles that were being waited on.
			$result["readfps"] = $this->ev_read_ready;
			$result["writefps"] = $this->ev_write_ready;
			$result["exceptfps"] = (is_array($exceptfps) ? array() : $exceptfps);

			$this->ProcessWaitResult($result);

			// Post-process clients.
			foreach ($result["clients"] as $id => $client)
			{
				$this->UpdateClientState($id);
			}

			return $result;
		}

		public function UpdateClientState($id)
		{
			if (isset($this->clients[$id]))
			{
				$client = $this->clients[$id];

				$events = 0;

				if ($client->writedata === "")  $events = Ev::READ;

				if ($client->writedata !== "" || ($client->websocket !== false && $client->websocket->NeedsWrite()))  $events |= Ev::WRITE;

				$this->ev_watchers["ws_c_" . $id]->set($client->fp, $events);
			}
		}

		public function RemoveClient($id)
		{
			parent::RemoveClient($id);

			if (isset($this->ev_watchers["ws_c_" . $id]))
			{
				$this->ev_watchers["ws_c_" . $id]->stop();

				unset($this->ev_watchers["ws_c_" . $id]);
			}
		}
	}
?>
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
