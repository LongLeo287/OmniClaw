# Knowledge Dump for cqrs-journey_2

## File: contributing.md
```
# Contributing
If you haven't already read through them, we recommend the starting with the [Azure contribution guidelines][azure-oss].

We will _consider_ any contributions that align with the stated goals of the project.

## Legal
You will need to complete a Contributor License Agreement (CLA). Briefly, this agreement testifies that you are granting us permission to use the submitted change according to the terms of the project's license, and that the work being submitted is under appropriate copyright.

Please submit a [Contributor License Agreement (CLA)](https://cla.azure.com/) before submitting a pull request. This process is automated and should be painless.

## Housekeeping
Your pull request should:

* Include a description of what your change intends to do.
* Be based on a reasonably recent commit in the `master` branch.
* Include tests covering your changes _as appropriate_.

## Be nice
We might be slower than you'd like. We might also ask you to make changes to the pull request. We ask for your patience.  :smiley:

[azure-oss]: http://azure.github.io/guidelines.html#contributing

```

## File: LICENSE.txt
```
==============================================================================================================
   Microsoft patterns & practices (http://msdn.microsoft.com/practices)
   CQRS Journey project
==============================================================================================================
   2012 Microsoft. All rights reserved. Certain content used with permission from contributors
   http://go.microsoft.com/fwlink/p/?LinkID=258575

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## File: _GIT_INGEST.md
```
# OmniClaw Repo Plow: CIV_FETCHED_cqrs-journey_134746



================================================
FILE: CONTRIBUTING.md
================================================
# Contributing
If you haven't already read through them, we recommend the starting with the [Azure contribution guidelines][azure-oss].

We will _consider_ any contributions that align with the stated goals of the project.

## Legal
You will need to complete a Contributor License Agreement (CLA). Briefly, this agreement testifies that you are granting us permission to use the submitted change according to the terms of the project's license, and that the work being submitted is under appropriate copyright.

Please submit a [Contributor License Agreement (CLA)](https://cla.azure.com/) before submitting a pull request. This process is automated and should be painless.

## Housekeeping
Your pull request should:

* Include a description of what your change intends to do.
* Be based on a reasonably recent commit in the `master` branch.
* Include tests covering your changes _as appropriate_.

## Be nice
We might be slower than you'd like. We might also ask you to make changes to the pull request. We ask for your patience.  :smiley:

[azure-oss]: http://azure.github.io/guidelines.html#contributing


================================================
FILE: LICENSE.txt
================================================
==============================================================================================================
   Microsoft patterns & practices (http://msdn.microsoft.com/practices)
   CQRS Journey project
==============================================================================================================
   2012 Microsoft. All rights reserved. Certain content used with permission from contributors
   http://go.microsoft.com/fwlink/p/?LinkID=258575

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

================================================
FILE: docs\images\readme.txt
================================================
SVG Diagrams created using Inkscape
EP Diagrams created using Evolus Pencil (desktop edition)

================================================
FILE: source\Conference\Conference.Web\Content\form\form.js
================================================
$.fn.jsSelect = function() {
	var JsSelect__template = '<div class="form-select-pad">' +
		'<div class="form-select js-select">' +
			'<span class="form-select__drop-down"><span></span></span>' +
			'<div class="form-select__active js-current"></div>' +
			'<div class="form-select__options js-options" style="display: none;"><ul class="form-select__options"></ul></div>' +
		'</div>' +	
		'<input class="js-input" type="hidden"/>' +
	'</div>';
	
	
	var $cont = null;
	var valueLabels = {};
	var isOptionsOpen = false;
	
	var init = function($select) {
		$cont = $(JsSelect__template);	
		initClassAndName($select);
		initOptions($select);
		setValue($select.val());
		$select.replaceWith($cont);
		//handlers
		$cont.find('.js-select').click(onClickSelect);
		$cont.find('.js-options li.form-select__options__item').click(onClickOption);
		$(document.body).click(onBodyClick);
	};
	
	var initClassAndName = function($select) {
		if($select[0].className) {
			$cont.addClass($select[0].className);
		}
		$cont.find('.js-input').attr('name', $select.attr('name'));
	};
	
	var initOptions = function($select) {
		var options = $select[0].options;
		$cont.find('.js-options ul').append('<li class="form-select__options__active-item js-current"></li>');
		for(var i=0; i<options.length; i++) {
			var option = options[i];
			valueLabels[option.value] = option.text;
			
			var $opt = $('<li class="form-select__options__item"/>');
			$opt.text(option.text);
			$opt.data('val', option.value);
			if(option.value == $select.val())
				$opt.hide();
			$cont.find('.js-options ul').append($opt);
		}
	};
	
	var setValue = function(value) {
		var label = valueLabels[value];
		$cont.find('.js-current').text(label);
		$cont.find('.js-input').val(value);
	};
	
	var onClickSelect = function() {
		if(!isOptionsOpen) {
			$cont.find('.js-options').show();
			isOptionsOpen = true;
			return false;
		}
	};
	
	var onBodyClick = function() {
		if(isOptionsOpen) {
			$cont.find('.js-options').hide();
			isOptionsOpen = false;
		}
	};
	
	var onClickOption = function() {
		setValue($(this).data('val'));
		$('.form-select__options__item').show();
		$(this).hide();
	};
	
	init(this);
};


$(function() {
	$('select').each(function(){
		$(this).jsSelect();
	});

    $(window).bind('form-reload', function(e, data) {
        data.$form.find('select').each(function(){
            $(this).jsSelect();
        });
    });
	
	$('.js-radiobutton').click(function(){
		$('.form__rb__item').removeClass('form__rb__item_a');
		$(this).addClass('form__rb__item_a');
		
		$('.js-radiobutton-box').hide();
		$('.nav__right-small').hide();
		$('.' + $(this).attr('name') + '-box').show();
		$('.' + $(this).attr('name') + '-proceed').show();
	});
	
	$('.js-checkbox').click(function(){
		$(this).toggleClass('form__chb__item_a');
	});
	
	$('.js-checkbox-seats').click(function(){
		$(this).toggleClass('form__chb__item_a');
		$('.form__seats-select').toggle();
	});
	
	$('.j-promocode-field').click(function(){
		$(this).hide();
		$('.form-promo').show();
		return false;
	});
	
	$('.js-select-chb').click(function(){
		$('.form-select-checkbox').toggle();
	});
	
});

$(function () {
    $('.inline-datepicker').each(function () {
        var $this = $(this);
        var picker = document.createElement('div');
        $this.after(picker);
        $(picker).datepicker({
            onSelect: function (dateText) {
                $this.val(dateText);
            },
            dateFormat: 'yy/mm/dd',
            defaultDate: $this.val()
        });
    });
});

================================================
FILE: source\Conference\Conference.Web\Content\tabs\tabs.js
================================================
$(function() {
	$('.js-reg-form').click(function(){
		$('.tabs__item').removeClass('tabs__item_active');
		$(this).addClass('tabs__item_active');
		
		$('.content').hide();
		$('.content_reg').show();
		return false;
	});
	$('.js-login-form').click(function(){
		$('.tabs__item').removeClass('tabs__item_active');
		$(this).addClass('tabs__item_active');
		
		$('.content').hide();
		$('.content_login').show();
		return false;
	});
});

================================================
FILE: source\Conference\Conference.Web\Scripts\_references.js
================================================
﻿/// <reference path="jquery-1.6.2.js" />

// ==============================================================================================================
// Microsoft patterns & practices
// CQRS Journey project
// ==============================================================================================================
// ©2012 Microsoft. All rights reserved. Certain content used with permission from contributors
// http://go.microsoft.com/fwlink/p/?LinkID=258575
// Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
// with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
// Unless required by applicable law or agreed to in writing, software distributed under the License is 
// distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
// See the License for the specific language governing permissions and limitations under the License.
// ==============================================================================================================

/// <reference path="jquery-ui-1.8.11.js" />
/// <reference path="jquery.validate.js" />
/// <reference path="knockout-2.0.0.debug.js" />
/// <reference path="modernizr-2.0.6-development-only.js" />

================================================
FILE: source\Conference\Conference.Web.Public\Content\form\form.js
================================================
// ==============================================================================================================
// Microsoft patterns & practices
// CQRS Journey project
// ==============================================================================================================
// 2012 Microsoft. All rights reserved. Certain content used with permission from contributors
// http://go.microsoft.com/fwlink/p/?LinkID=258575
// Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
// with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
// Unless required by applicable law or agreed to in writing, software distributed under the License is 
// distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
// See the License for the specific language governing permissions and limitations under the License.
// ==============================================================================================================

$.fn.jsSelect = function() {
	var JsSelect__template = '<div class="form-select-pad">' +
		'<div class="form-select js-select">' +
			'<span class="form-select__drop-down"><span></span></span>' +
			'<div class="form-select__active js-current"></div>' +
			'<div class="form-select__options js-options" style="display: none;"><ul class="form-select__options"></ul></div>' +
		'</div>' +	
		'<input class="js-input" type="hidden"/>' +
	'</div>';
	
	
	var $cont = null;
	var valueLabels = {};
	var isOptionsOpen = false;
	
	var init = function($select) {
		$cont = $(JsSelect__template);	
		initClassAndName($select);
		initOptions($select);
		setValue($select.val());
		$select.replaceWith($cont);
		//handlers
		$cont.find('.js-select').click(onClickSelect);
		$cont.find('.js-options li.form-select__options__item').click(onClickOption);
		$(document.body).click(onBodyClick);
	};
	
	var initClassAndName = function($select) {
		if($select[0].className) {
			$cont.addClass($select[0].className);
		}
		$cont.find('.js-input').attr('name', $select.attr('name'));
	};
	
	var initOptions = function($select) {
		var options = $select[0].options;
		$cont.find('.js-options ul').append('<li class="form-select__options__active-item js-current"></li>');
		for(var i=0; i<options.length; i++) {
			var option = options[i];
			valueLabels[option.value] = option.text;
			
			var $opt = $('<li class="form-select__options__item"/>');
			$opt.text(option.text);
			$opt.data('val', option.value);
			if(option.value == $select.val())
				$opt.show();
			$cont.find('.js-options ul').append($opt);
		}
	};
	
	var setValue = function(value) {
		var label = valueLabels[value];
		$cont.find('.js-current').text(label);
		$cont.find('.js-input').val(value).change();
	};
	
	var onClickSelect = function() {
		if(!isOptionsOpen) {
			$cont.find('.js-options').show();
			isOptionsOpen = true;
			return false;
		}
	};
	
	var onBodyClick = function() {
		if(isOptionsOpen) {
			$cont.find('.js-options').hide();
			isOptionsOpen = false;
		}
	};
	
	var onClickOption = function() {
		setValue($(this).data('val'));
		$('.form-select__options__item').show();
	};
	
	init(this);
};


$(function() {
	$('select').each(function(){
		$(this).jsSelect();
	});

    $(window).bind('form-reload', function(e, data) {
        data.$form.find('select').each(function(){
            $(this).jsSelect();
        });
    });
	
	$('.js-radiobutton input').change(function(){
		$('.js-radiobutton-box').hide();
		$('.nav__right-small').hide();
		$('.js-radiobutton input:checked').each(function () {
		    var name = $(this).parent().attr('name');
		    $('.' + name + '-box').show();
		    $('.' + name + '-proceed').show();
		});
	});
	
	$('.js-checkbox').click(function(){
		$(this).toggleClass('form__chb__item_a');
	});
	
	$('.js-checkbox-seats').click(function(){
		$(this).toggleClass('form__chb__item_a');
		$('.form__seats-select').toggle();
	});
	
	$('.j-promocode-field').click(function(){
		$(this).hide();
		$('.form-promo').show();
		return false;
	});
});

================================================
FILE: source\Conference\Conference.Web.Public\Content\reg-time-info\reg-time-info.js
================================================
// ==============================================================================================================
// Microsoft patterns & practices
// CQRS Journey project
// ==============================================================================================================
// 2012 Microsoft. All rights reserved. Certain content used with permission from contributors
// http://go.microsoft.com/fwlink/p/?LinkID=258575
// Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
// with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
// Unless required by applicable law or agreed to in writing, software distributed under the License is 
// distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
// See the License for the specific language governing permissions and limitations under the License.
// ==============================================================================================================

$(function() {
  var w = $(window);
  var rti = $('.reg-time-info');
    var currentScrollTop = 0;
	w.scroll(function(){ 
		currentScrollTop = w.scrollTop() - 285;
		rti.css('top', currentScrollTop > 0 ? currentScrollTop : 0);
    });


	var Conference = {};

    Conference.StartTimer = function(element, timeoutCallback, formatCallback) {
        timeoutCallback = (typeof timeoutCallback === 'undefined') ? Conference._DefaultTimeoutCallback(element) : timeoutCallback;
        formatCallback = (typeof formatCallback === 'undefined') ? Conference._DefaultFormatCallback : formatCallback;

        var targetDate = new Date(parseInt(element.getAttribute('data-targetDate')));

        var timerCallback = function() {
            var formattedMilliseconds = '';
            var currentDate = new Date();

            var dateDiff = targetDate.getTime() - currentDate.getTime();
            if (dateDiff > 0) {
                formattedMilliseconds = formatCallback(dateDiff);
                element.innerHTML = formattedMilliseconds;
                window.setTimeout(function() { timerCallback(); }, 1000);
            } else {
                timeoutCallback();
            }
        };

        timerCallback();
    };

    Conference._DefaultFormatCallback = function(milliseconds) {
        var totalSeconds = Math.floor(milliseconds / 1000);
        var seconds = totalSeconds % 60;
        var totalMinutes = Math.floor(totalSeconds / 60);
        var minutes = totalMinutes % 60;
        var totalHours = Math.floor(totalMinutes / 60);
        var hours = totalHours % 24;
        var days = Math.floor(totalHours / 24);

        var secondsPart = [((seconds >= 10) ? '' : '0'), seconds.toString()].join('');
        var minutesPart = [((minutes >= 10) ? '' : '0'), minutes.toString()].join('');
        var hoursPart = [((hours >= 10) ? '' : '0'), hours.toString()].join('');
        var daysPart = [((days >= 10) ? '' : '0'), days.toString()].join('');

        var result = '';

        if (days > 0) {
            result = [daysPart, hoursPart, minutesPart, secondsPart].join(':');
        } else if (hours > 0) {
            result = [hoursPart, minutesPart, secondsPart].join(':');
        } else {
            result = [minutesPart, secondsPart].join(':');
        }

        return result;
    };

    Conference._DefaultTimeoutCallback = function(element) {
        return function() {
            element.innerHTML = '';
        };
    };

    $('.reg-time-info__title').each(function() {
        var redirectUrl = this.getAttribute('data-redirectUrl');
        Conference.StartTimer(this, function() { window.location = redirectUrl; });
    });
});

================================================
FILE: source\Conference\Conference.Web.Public\Scripts\main.js
================================================
// ==============================================================================================================
// Microsoft patterns & practices
// CQRS Journey project
// ==============================================================================================================
// 2012 Microsoft. All rights reserved. Certain content used with permission from contributors
// http://go.microsoft.com/fwlink/p/?LinkID=258575
// Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
// with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
// Unless required by applicable law or agreed to in writing, software distributed under the License is 
// distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
// See the License for the specific language governing permissions and limitations under the License.
// ==============================================================================================================

$(document).ready(function(){
	$.fn.cycle.defaults.speed   = 900;
	$.fn.cycle.defaults.timeout = 6000;
	
	var RSec = 0;
	var RTile = 0;
	
	$('.tile-slide').each(function(index) {
		$(this).cycle({
			fx:      'scrollDown', 
			speed:    400, 
			timeout:  0
        });
    });
	
	AnimateTile();
	
	function AnimateTile() {
		RSec = Math.floor(Math.random() *5000) + 1000;
		RTile = Math.floor(Math.random() *5);
		setTimeout(function() {						  
			  $('.tile-slide').eq(RTile).cycle('next');
			  AnimateTile();
			}, RSec);
	}
	
	/*
	var RSec = 0;
	$('.tile-slide').each(function(index) {
		RSec = Math.floor(Math.random() *20000) + 3000
		$(this).cycle({
			fx:      'scrollDown', 
			speed:    400, 
			timeout:  RSec
		});
	});
	*/
	
	
	/*var SliderPos = 0;
	var SliderLen = 0;
	var AnimateSpeed = 500;
	var AnimateDelay = AnimateSpeed + 800;
	$('.tile__imgs').each(function(index) {
		$(this).find('img').css({'display': 'none','z-index': 1,'opacity': 0});
		SliderLen = $(this).find('img').length;
		$(this).find('img:first').css({'display': 'block','z-index': SliderLen+1,'opacity': 1});
	});
	
	var hTimer = null;

	$(".tile").mouseenter(function(){
	  var self = this;
	  SliderPos = 0;
	  SliderLen = $(self).find('.tile__imgs>*').length;
	  
	  if(hTimer != null) clearInterval(hTimer);
	  
	  hTimer = setInterval(function() {						  
		  if(SliderLen!=SliderPos+1){
			$(self).find('.tile__imgs>*').eq(SliderPos).css({'display': 'block','z-index': SliderLen});
			$(self).find('.tile__imgs>*').eq(SliderPos+1).css({'display': 'block','z-index': SliderLen+1});
			$(self).find('.tile__imgs>*').eq(SliderPos).animate({'opacity': 0},AnimateSpeed);
			$(self).find('.tile__imgs>*').eq(SliderPos+1).animate({'opacity': 1},AnimateSpeed);
			$(self).find('.tile__imgs>*').eq(SliderPos).css({'display': 'block','z-index': 1});
			SliderPos++;
			} else {
				$(self).find('.tile__imgs>*').eq(SliderPos).css({'display': 'block','z-index': SliderLen});
				$(self).find('.tile__imgs>*').eq(0).css({'display': 'block','z-index': SliderLen+1});
				$(self).find('.tile__imgs>*').eq(SliderPos).animate({'opacity': 0},AnimateSpeed);
				$(self).find('.tile__imgs>*').eq(0).animate({'opacity': 1},AnimateSpeed);
				$(self).find('.tile__imgs>*').eq(SliderPos).css({'display': 'block','z-index': 1});
				SliderPos = 0;
			}
		}, AnimateDelay);				  
	}).mouseleave(function(){
	   if(hTimer != null) {
		 clearInterval(hTimer);
		 hTimer = null;
	   }
	   var self = this;
	   $(self).find('.tile__imgs>*').stop();
	   $(self).find('.tile__imgs>*').css({'display': 'none','z-index': 1,'opacity': 0});
	   $(self).find('.tile__imgs>*:first').css({'display': 'block','z-index': SliderLen+1,'opacity': 1});

	});*/

});

$(function () {
    function getTweets() {
        var $tweets = $("#tweets");
        if ($tweets.length > 0) {
            var search = $tweets.attr("data-search");
            var url = 'http://search.twitter.com/search.json?callback=?&q=' + search;
            $.getJSON(url, function(json) {
                var output = [];
                if (json.results) {
                    for (var i = 0, len = Math.min(json.results.length, 10); i < len; i++) {

                        var timeDifference = (new Date().getTime() - Date.parse(json.results[i].created_at)) / (60 * 1000);
                        var time;
                        if (timeDifference < 60) {
                            time = Math.round(timeDifference) + "m ago";
                        } else {
                            timeDifference = timeDifference / 60;
                            if (timeDifference < 24) {
                                time = Math.round(timeDifference) + "h ago";
                            } else {
                                time = Math.round(timeDifference / 24) + "d ago";
                            }
                        }
                        output.push('<span class="t

================================================
FILE: source\Migrations\Migrations-Readme.txt
================================================
IMPORTANT NOTE
--------------

The projects in this folder are not referenced by the final solution, and they do not build with the current 
state of the codebase. This is intentional.
They correspond to specific milestones in the journey and only make sense within the context of migrations from 
version to version. To reproduce the migration experience, please check out specific versions of the entire 
system tagged V2-pseudo-prod or V3-pseudo-prod in the git repository history.

See the Migration notes (http://go.microsoft.com/fwlink/?LinkID=259596) and chapters 6 and 7 of the Guide:
http://go.microsoft.com/fwlink/p/?LinkID=258556
http://go.microsoft.com/fwlink/p/?LinkID=258557
```

## File: docs\images\readme.txt
```
SVG Diagrams created using Inkscape
EP Diagrams created using Evolus Pencil (desktop edition)
```

## File: source\Conference\Conference.Web\Content\style.css
```
@import "common/common.css";
@import "page/page.css";
@import "quick/quick.css";
@import "footer/footer.css";
@import "likes/likes.css";
@import "content-main/content-main.css";
@import "tile/tile.css";
@import "time-n-place/time-n-place.css";
@import "menu/menu.css";
@import "content/content.css";
@import "nav/nav.css";
@import "form/form.css";
@import "tabs/tabs.css";
```

## File: source\Conference\Conference.Web\Content\common\common.css
```
h1, h2, h3, h4, h5, h6, p, blockquote, pre, a, abbr, acronym, address, big, cite, code, del, dfn, em, img, ins, kbd, q, s, samp, small, strike, sub, sup, tt, var, b, u, i, center, dl, dt, dd, ol, ul, li, fieldset, form, label, legend, table, caption, tbody, tfoot, thead, tr, th, td {
    margin: 0;
    padding: 0;
    border: 0;
    outline: 0;
    font-weight: normal;
    text-align: left;
    vertical-align: baseline;
    background: transparent;
    font-size: 100%;
    line-height: 16px;}
ol, ul { list-style: none; }
table { border-collapse: collapse; border-spacing: 0;}
html {
    overflow-x: visible;
    overflow-y: scroll;
    height: 100%;
}
body {
    margin: 0;
    padding: 0;
    font-family: "Segoe UI", "Arial", sans-serif;
    font-size: 13px;
    line-height: 16px;
}
label, input[type="button"], input[type="submit"], button {
    cursor: pointer;
}
input, select, button, textarea {
    font-family: "Segoe UI", "Arial", sans-serif;
    margin: 0;
}
input[type="radio"] {
    margin: 0;
}
select {
    height: 22px;
}
blockquote, q {
    quotes: none;
}
blockquote:before, blockquote:after,
q:before, q:after {
    content: '';
    content: none;
}
/*ссылки*/
a{outline: none; color: #fff;text-decoration: underline;}
a:hover {color: #66ccff;}
/*очистка*/
.g-clear {overflow: hidden;clear: both;font-size: 0; height: 0;}

input {
    text-align: left;
}
input[type=tel],
input[type=text],
input[type=number] {
    border-radius: 0;
    -webkit-border-radius: 0;
}



/* Styles for validation helpers
-----------------------------------------------------------*/
.field-validation-error
{
    color: #ff0000;
}

.field-validation-valid
{
    display: none;
}

.input-validation-error
{
    border: 1px solid #ff0000;
    background-color: #ffaaaa;
}

.validation-summary-errors
{
    font-weight: bold;
    color: #FFFF00;
}

.validation-summary-valid
{
    display: none;
}
```

## File: source\Conference\Conference.Web\Content\content\content.css
```
.content {
    background: #2f7d00;
    min-height: 30px;
    padding: 20px;
}
.content_login {
	width: 320px;
	padding-left: 150px;
	padding-top: 10px;
	margin-top: 20px;
	background: #2f7d00 url(content_login.gif) 38px 37px no-repeat;
	}
.content_reg {
	width: 320px;
	padding-left: 150px;
	padding-top: 10px;
	margin-top: 20px;
	background: #2f7d00 url(content_reg.gif) 38px 37px no-repeat;
	display: none;
	}
.content_error {
	background: #cc6600;
	}
.content_error__txt {
	font-size: 15px;
	}
.content p {
    padding-top: 5px;
    line-height: 18px;
}
.content h3 {
    font-size: 20px;
    line-height: 1;
    padding-top: 21px;
    padding-bottom: 20px;
}
.content table {
    width: 100%;
    vertical-align: top;
}
.content th {
    padding: 5px 25px 8px 10px;
    background: #205501;
    border-bottom: 1px solid #2f7d00;
    vertical-align: top;
    font-size: 13px;
}
.content td {
    padding: 13px 20px 18px 10px;
    border-bottom: 1px solid #2f7d00;
    
    background: #fff;
    color: #000;
    vertical-align: top;
    font-size: 15px;
}
.content .content__table_seats-edit td {
	color: #8d9092;
	}
.content__link_pseudo {
    color: #0066cc;
    border-bottom: 1px dashed;
    text-decoration: none;
    line-height: 15px;
    display: inline-block;
}
.content .content__table-cell_right {
    text-align: right;
    padding-right: 0;
}
.content .content__table-cell_left {

}
.content__table_first-cell-wide td:first-child {
    width: 255px;
}

.content .content__note {
    letter-spacing: -1px;
    color: #999999;
    line-height: 13px;
    font-size: 11px;
}
.content .content__cell_total {
    font-weight: bold;
    font-size: 20px;
}
.content select{
    width: 61px;
}
.content tr.content__table__error td {
    border-top: solid 2px #ff6600;
	border-bottom: solid 2px #ff6600;
}
.content tr.content__table__error td:first-child {
    background: #fff url(content__table__error.gif) left top repeat-y;
}
.content tr.content__table__error td:last-child {
    background: #fff url(content__table__error.gif) right top repeat-y;
}
.content td.content__table__error-info {
	background: #ff6600;
	width: auto;
	color: #fff;
	padding: 2px 20px 3px 10px;
	line-height: 33px;
	}
.content .content__table__h2 td {
	color: #ffffff;
	font-size: 20px;
	background: none;
	}
.content td a,.content td a:active,.content td a:visited,.content td a:hover,
.content .content__table_seats-edit .seats__edit td a,.content .content__table_seats-edit .seats__edit td a:active,.content .content__table_seats-edit .seats__edit td a:visited,.content .content__table_seats-edit .seats__edit td a:hover {
	color: #0156ab;
	}
.content .content__table_seats-edit td a,.content .content__table_seats-edit td a:active,.content .content__table_seats-edit td a:visited,.content .content__table_seats-edit td a:hover {
	color: #80aad5;
	}
.content td a.red,.content td a.red:active,.content td a.red:visited,.content td a.red:hover {
	color: #cc3300;
	}
.content .content__table_seats-edit td a.red,.content .content__table_seats-edit td a.red:active,.content .content__table_seats-edit td a.red:visited,.content .content__table_seats-edit td a.red:hover {
	color: #e5997f;
	}
.content td a.green,.content td a.green:active,.content td a.green:visited,.content td a.green:hover {
	color: #2f7d00;
	}
.content .content__table_seats-edit td a.green,.content .content__table_seats-edit td a.green:active,.content .content__table_seats-edit td a.green:visited,.content .content__table_seats-edit td a.green:hover {
	color: #7da466;
	}
/*.content .content__table__grey td {
	background: #cccccc;
	}*/
.content table tr:nth-child(even) td {
	background: #eeeeee;
	}
.content .content__table__pub {
	width: 70px;
	padding-right: 0;
	}
.content .content__table__delete {
	width: 50px;
	padding-left: 5px
	}

.content .seats-type__name a,.content .seats-type__name a:visited,.content .seats-type__name a:active,.content .seats-type__name a:hover {
	text-decoration: none;
	border-bottom: dotted 1px #4180c0;
	}
.content .content__table_seats-edit .seats-type__name a,.content .content__table_seats-edit .seats-type__name a:visited,.content .content__table_seats-edit .seats-type__name a:active,.content .content__table_seats-edit .seats-type__name a:hover {
	text-decoration: none;
	border-bottom: dotted 1px #a0bfdf;
	color: #80aad5;
	}
.content .seats-type-add a,.content .seats-type-add a:visited,.content .seats-type-add a:active,.content .seats-type-add a:hover {
	text-decoration: none;
	border-bottom: dotted 1px #4180c0;
	}
.content__table__also-req {
	width: 150px;
	}
.content .seats__edit td {
	border-bottom: none;
	}
.content .seats__edit {
	display: none;
	}
.content .seats__edit .form__but-box {
	margin: 0; padding: 0;
	text-align: center;
	}
.content .seats__edit .form__but-box .form__but {
	margin: 0 10px 0;
	}
.content .seats__edit td {
	padding: 12px 10px 12px 4px;
	line-height: 25px;
	}
.content .seats__edit .form__field {
	margin: 0 0 0 0;
	}
.content .seats__edit a,.content .seats__edit a:active,.content .seats__edit a:visited,.content .seats__edit a:hover {
	text-decoration: none;
	border-bottom: dotted 1px #4180c0;
	}
.content .seats__edit.form-select-pad {
	top: 0;
	}
	
	
.content__create-conf {
	
	}
.content__create-conf a,.content__create-conf a:visited,.content__create-conf a:active,.content__create-conf a:hover {
	float: right;
	margin: -105px -20px 0 0;
	position: relative;
	
	display: block;
	background: #2f7d00 url(content__create-conf.gif) 10px 10px no-repeat;
	height: 40px;
	line-height: 36px;
	font-size: 28px;
	text-decoration: none;
	font-family: Segoe UI Light;
	padding: 0 20px 0 48px;
	
	color: #fff;
	}
.content__create-conf a:hover {
	margin: -110px -25px 0 0;
	
	border: solid 5px #2f7d00;
	
	text-decoration: none;
	
	color: #fff;
	}
.avail-from,.avail-to {
	color: #272727;
	border-bottom: dotted 1px #272727;
	cursor: pointer;
	}
```

## File: source\Conference\Conference.Web\Content\content-main\content-main.css
```
.content-main {
    min-height: 355px;
    position: relative;
}
.content-main__wrapper {
    float: left;
    width: 1130px;
    }
    .content-main__main {
        margin: 0 425px 0 250px;
    }
    *:first-child+html .content-main__main {
        zoom:1;
        padding-bottom: 10px;
    }

.content-main__aside {
    float: left;
    width: 250px;
    margin-left: -1130px;
    padding-bottom: 170px;
}
.content-main__extra {
    float: left;
    width: 425px;
    margin-left: -425px;
}

.content-main_register, .content-main_create-conf {width: 1020px;padding: 0;}
.page_conference-seats .content-main__wrapper,
.page_conference .content-main__wrapper,
.page_create-conf .content-main__wrapper,
.content-main_register .content-main__wrapper {
    width: auto;
    float: none;
    }
    *:first-child+html .page_conference .content-main__main,
    *:first-child+html .page_create-conf .content-main__main,
    *:first-child+html .content-main_register .content-main__main {padding: 0; }
    .page_create-conf .content-main__main,
    .content-main_register .content-main__main {
        float: left;
        margin: 0;
        width: 700px;
        }
	.page_conference-seats .content-main__main,
	.page_conference .content-main__main {
        float: none;
        margin: 0;
        width: auto;
        }
.page_conference .content-main__aside,
.page_create-conf .content-main__aside,
.content-main_register .content-main__aside {
    float: right;
    width: 300px;
    margin: 0;
    padding: 0;
}


.content-main__time-n-place {
    height: 175px;
    margin-top: -175px;
    position: absolute;
}

.content-main__header {
    font-size: 28px;
    line-height: 27px;
    height: 40px;
    padding-bottom: 5px;
    font-family: "Segoe UI light", Arial, sans-serif;
    overflow: hidden;
	padding-top: 34px;
}
.content-main__extra-right {
    float: right;
}
.content-main__extra-left {
    float: left;
    width: 260px;
}
.content-main__nav {
    padding: 21px 19px 10px;
}
```

## File: source\Conference\Conference.Web\Content\footer\footer.css
```
/*
==============================================================================================================
Microsoft patterns & practices
CQRS Journey project
==============================================================================================================
2012 Microsoft. All rights reserved. Certain content used with permission from contributors
http://go.microsoft.com/fwlink/p/?LinkID=258575
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is 
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and limitations under the License.
==============================================================================================================
*/

.footer {
	min-height: 100px;
    width: 1130px;
	margin: 0 auto 0;
	}
footer {
	font-size: 11px;
	min-height: 100px;
    width: 1130px;
    margin: 55px auto 0;
}
.footer__logo {
    margin: 1px 0 0 -2px;
    float: left;
}
.footer__content {
    margin-left: 250px;
}
.footer__content p {padding-top: 12px;}
.footer__content p:first-child {padding-top: 0;}
.footer__content a {
    text-decoration: none;
    border-bottom: 1px solid;
}
.footer__disclaimer {
    text-transform: uppercase;
    color:bisque;
    font-weight: bold;
}
```

## File: source\Conference\Conference.Web\Content\form\form.css
```
.form {
	
	}
.form__fieldset {
	margin: 0; padding: 0;
	width: 320px;
	}
.form__fieldset:nth-child(odd) {
	float: left;
	}
.form__fieldset:nth-child(even) {
	float: right;
	}
.form__col3 {
	margin: 0 0 0 -20px;
	}
.form__col3 .form__fieldset:first-child {
	float: left;
	width: 170px;
	margin: 0 0 0 20px;
	}
.form__col3 .form__fieldset {
	float: left;
	width: 195px;
	margin: 0 0 0 40px;
	}
.form__fieldset_textarea {
	float: none;
	width: 100%;
	}
.content_login .form__fieldset {
	float: none;
	}
.content_reg .form__fieldset {
	float: none;
	}
.form__label, label {
	font-size: 15px;
	padding: 15px 0 0;
	display: block;
	}
.form__field {
	border: solid 1px #abadb3;
	/*padding: 0 7px 0;*/
	padding: 0 0px 0;
	background: #fff;
	margin: 3px 0 0;
	}
.form__field input {
	width: 100%;
	margin: 0 0 0 0;
	text-align: left;
	border: none; 
    padding: 0 7px;
    /*padding: 0;*/
	font-size: 15px;
	color: #333333;
	height: 24px; line-height: 24px;
	}
.form__field pre {
	width: 100%;
	margin: 0 0 0 0;
	text-align: left;
	border: none;
    padding: 0 7px;
    /*padding: 0;*/
	font-size: 15px;
	color: #777777;
    font-weight: 500;
	height: 24px; line-height: 24px;
    font-family: "Segoe UI", "Arial", sans-serif;
    background-color: #DDDDDD
	}
.form__field textarea {
	height: 117px;
	width: 100%;
	margin: 0 0 0 0;
	text-align: left;
	border: none; 
    padding: 5px 7px;
    /*padding: 5px 0;*/
	font-size: 15px;
	color: #333333;
	line-height: 24px;
	}
.form__field_file {
	width: 229px;
	}
.form__field_file-input {
	position: absolute;
	width: 320px;
	height: 26px;
	margin: -1px 0 0 -8px;
	cursor: pointer;
	}
.form__field_file-input input {
	opacity: 0; filter: alpha(opacity: 0);
	position: absolute;
	left: 0;
	top: 0;
	width: 100%;
	height: 100%;
	cursor: pointer;
	}
.form__field_file-input * {
	cursor: pointer;
	}
.form__rb_m {
	margin: 10px 0 15px 0;
	}
.form__rb {
	
	}
.form__rb__title {
	display: inline;
	font-size: 15px;
	padding: 0 20px 0 0;
	}
.form__rb__item {
	background: url(form__rb__item.png) left 2px no-repeat;
	padding: 0 15px 0 25px;
	font-size: 15px;
	}
.form__rb__item_a {
	background: url(form__rb__item_a.png) left 2px no-repeat;
	}
.form__chb {
	margin: 15px 0 0;
	}
.form__chb_seats {
	line-height: 30px;
	}
.form__chb__item {
	background: url(form__chb__item.png) left 0 no-repeat;
	padding: 0 0 0 35px;
	line-height: 20px;
	font-size: 15px;
	}
.seats__edit .form__chb__item {
	color: #272727;
	}
div.form__chb__item {
	background: url(form__chb__item.png) left 0 no-repeat;
	cursor: pointer;
	display: inline;
	}
.form__chb__item_a {
	background: url(form__chb__item_a.png) left 0 no-repeat;
	}
div.form__chb__item_a {
	background: url(form__chb__item_a.png) left 0 no-repeat;
	}
.form__chb_seats {
	padding: 0 0 0;
	height: 31px;
	line-height: 40px;
	}
.form__chb_remember {
	float: right;
	margin-top: 23px;
	}
.form__seats-select {
	display: inline;
	line-height: 20px;
	font-size: 15px;
	display: none;
	}
.form .form-select-pad {
	top: 0;
	margin: 3px 0 0;
	}
.form-select-pad {
	position: relative;
	top: -5px;
	}
.seats__edit .form-select-pad, .form__seats-select .form-select-pad {
	top: 0;
	display: inline-block;
	}
.form-select {
	border: solid 1px #abadb3;
	position: relative;
	height: 24px;
	min-width: 59px;
	background: #ffffff;
	}
.form__seats-select .form-select {
	display: inline-block;
	}
.form__seats-select .form-select__drop-down {
	background: #b42f03 url(form-select__drop-down.png) 50% 9px no-repeat;
	}
.form-select__drop-down,.form__seats-select_green .form-select__drop-down {
	position: absolute;
	right: 1px;
	top: 1px;
	width: 22px; height: 22px;
	background: #205501 url(form-select__drop-down.png) 50% 9px no-repeat;
	cursor: pointer;
	}
.form-select__active {
	height: 24px;
	line-height: 24px;
	color: #1c2126;
	font-size: 15px;
	padding: 0 30px 0 5px;
	cursor: pointer;
	}
div.form-select__options {
	background: #fff;
	border: solid 1px #abadb3;
	position: absolute;
	left: -1px;
	top: 24px;
	width: 100%;
	max-height: 124px;
	overflow: auto;
	z-index: 1000;
	}
.form-select__options__active-item,.form-select__options__item {
	height: 24px;
	line-height: 24px;
	color: #1c2126;
	font-size: 15px;
	padding: 0 5px 0 5px;
	}
.form-select__options__active-item:hover,.form-select__options__item:hover {
	background: #ddd;
	}
.form-select__options__active-item {
	display: none;
	}
	
.form-select-checkbox {
	position: absolute;
	right: -1px;
	top: 25px;
	background: #ffffff;
	border: solid 1px #abadb3;
	min-width: 200%;
	display: none;
	}
.form-select .form__chb__item {
	background: url(form__select-chb__item.gif) left 0 no-repeat;
	margin-left: 5px;
	line-height: 18px;
	margin-top: 7px;
	margin-bottom: 7px;
	display: block;
	padding: 0 0 2px 30px;
	}
.form-select .form__chb__item_a {
	background: url(form__select-chb__item_a.gif) left 0 no-repeat;
	}

	
.form-promo {
	display: none;
	height: 26px;
	margin: -3px 0 0;
	}
.form-promo__txt {
	width: 175px;
	height: 24px;
	border: solid 1px #abadb3;
	font-size: 15px;
	line-height: 24px;
	color: #1c2126;
	float: left;
	margin-right: 5px;
	padding: 0 7px;
	text-align: left;
	}
.form-promo__but {
	width: 66px;
	height: 26px;
	color: #fff;
	background: #205501;
	font-size: 15px;
	line-height: 26px;
	border: none;
	}
	
.form__but-box {
	margin: 20px 0 0;
	}
.form__but-box_file {
	float: right;
	margin: 3px 0 0;
	}
.form__but {
	background: #205501;
	border: none;
	color: #ffffff;
	font-family: Segoe UI;
	font-size: 15px;
	height: 26px;
	line-height: 16px;
	}
	
.form__forgot-link {
	float: right;
	margin: 25px 0 0;
	font-size: 15px;
	}
	
.form__file-logo {
	position: absolute;
	left: 50%;
	top: 207px;
	margin: 0 0 0 207px;
	width: 140px; height: 140px;
	background: #fff;
	text-align: center;
	}
.form__file-logo__valign {
	display: inline-block;
	height: 140px;
	vertical-align: middle;
	}
.form__file-logo__txt {
	background: #2f7d00;
	opacity: 0.85; filter: alpha(opacity: 85);
	position: absolute;
	left: 0;
	bottom: 0;
	width: 80%;
	color: #ffffff;
	font-size: 18px;
	padding: 9px 10% 12px;
	text-align: left;
	}
	
.datapicker-abs {
	display: none;
	padding: 15px 20px;
	border: solid 1px #fff;
	background: #2f7d00;
	}
```

## File: source\Conference\Conference.Web\Content\form\form.js
```
$.fn.jsSelect = function() {
	var JsSelect__template = '<div class="form-select-pad">' +
		'<div class="form-select js-select">' +
			'<span class="form-select__drop-down"><span></span></span>' +
			'<div class="form-select__active js-current"></div>' +
			'<div class="form-select__options js-options" style="display: none;"><ul class="form-select__options"></ul></div>' +
		'</div>' +	
		'<input class="js-input" type="hidden"/>' +
	'</div>';
	
	
	var $cont = null;
	var valueLabels = {};
	var isOptionsOpen = false;
	
	var init = function($select) {
		$cont = $(JsSelect__template);	
		initClassAndName($select);
		initOptions($select);
		setValue($select.val());
		$select.replaceWith($cont);
		//handlers
		$cont.find('.js-select').click(onClickSelect);
		$cont.find('.js-options li.form-select__options__item').click(onClickOption);
		$(document.body).click(onBodyClick);
	};
	
	var initClassAndName = function($select) {
		if($select[0].className) {
			$cont.addClass($select[0].className);
		}
		$cont.find('.js-input').attr('name', $select.attr('name'));
	};
	
	var initOptions = function($select) {
		var options = $select[0].options;
		$cont.find('.js-options ul').append('<li class="form-select__options__active-item js-current"></li>');
		for(var i=0; i<options.length; i++) {
			var option = options[i];
			valueLabels[option.value] = option.text;
			
			var $opt = $('<li class="form-select__options__item"/>');
			$opt.text(option.text);
			$opt.data('val', option.value);
			if(option.value == $select.val())
				$opt.hide();
			$cont.find('.js-options ul').append($opt);
		}
	};
	
	var setValue = function(value) {
		var label = valueLabels[value];
		$cont.find('.js-current').text(label);
		$cont.find('.js-input').val(value);
	};
	
	var onClickSelect = function() {
		if(!isOptionsOpen) {
			$cont.find('.js-options').show();
			isOptionsOpen = true;
			return false;
		}
	};
	
	var onBodyClick = function() {
		if(isOptionsOpen) {
			$cont.find('.js-options').hide();
			isOptionsOpen = false;
		}
	};
	
	var onClickOption = function() {
		setValue($(this).data('val'));
		$('.form-select__options__item').show();
		$(this).hide();
	};
	
	init(this);
};


$(function() {
	$('select').each(function(){
		$(this).jsSelect();
	});

    $(window).bind('form-reload', function(e, data) {
        data.$form.find('select').each(function(){
            $(this).jsSelect();
        });
    });
	
	$('.js-radiobutton').click(function(){
		$('.form__rb__item').removeClass('form__rb__item_a');
		$(this).addClass('form__rb__item_a');
		
		$('.js-radiobutton-box').hide();
		$('.nav__right-small').hide();
		$('.' + $(this).attr('name') + '-box').show();
		$('.' + $(this).attr('name') + '-proceed').show();
	});
	
	$('.js-checkbox').click(function(){
		$(this).toggleClass('form__chb__item_a');
	});
	
	$('.js-checkbox-seats').click(function(){
		$(this).toggleClass('form__chb__item_a');
		$('.form__seats-select').toggle();
	});
	
	$('.j-promocode-field').click(function(){
		$(this).hide();
		$('.form-promo').show();
		return false;
	});
	
	$('.js-select-chb').click(function(){
		$('.form-select-checkbox').toggle();
	});
	
});

$(function () {
    $('.inline-datepicker').each(function () {
        var $this = $(this);
        var picker = document.createElement('div');
        $this.after(picker);
        $(picker).datepicker({
            onSelect: function (dateText) {
                $this.val(dateText);
            },
            dateFormat: 'yy/mm/dd',
            defaultDate: $this.val()
        });
    });
});
```

## File: source\Conference\Conference.Web\Content\form\ui\index.html
```
<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
		<title>jQuery UI Example Page</title>
		<link type="text/css" href="css/custom-theme/jquery-ui-1.8.19.custom.css" rel="stylesheet" />
		<script type="text/javascript" src="js/jquery-1.7.2.min.js"></script>
		<script type="text/javascript" src="js/jquery-ui-1.8.19.custom.min.js"></script>
		<script type="text/javascript">
			$(function(){

				// Datepicker
				$('#datepicker').datepicker({
					inline: true
				});

				//hover states on the static widgets
				$('#dialog_link, ul#icons li').hover(
					function() { $(this).addClass('ui-state-hover'); },
					function() { $(this).removeClass('ui-state-hover'); }
				);

			});
		</script>
		<style type="text/css">
			/*demo page css*/
			body{ font: 62.5% "Trebuchet MS", sans-serif; margin: 50px;}
			.demoHeaders { margin-top: 2em; }
			#dialog_link {padding: .4em 1em .4em 20px;text-decoration: none;position: relative;}
			#dialog_link span.ui-icon {margin: 0 5px 0 0;position: absolute;left: .2em;top: 50%;margin-top: -8px;}
			ul#icons {margin: 0; padding: 0;}
			ul#icons li {margin: 2px; position: relative; padding: 4px 0; cursor: pointer; float: left;  list-style: none;}
			ul#icons span.ui-icon {float: left; margin: 0 4px;}
		</style>
	</head>
	<body>
	<h1>Welcome to jQuery UI!</h1>
	<p style="font-size: 1.3em; line-height: 1.5; margin: 1em 0; width: 50%;">This page demonstrates the widgets you downloaded using the theme you selected in the download builder. We've included and linked to minified versions of <a href="js/jquery-1.7.2.min.js">jQuery</a>, your personalized copy of <a href="js/jquery-ui-1.8.19.custom.min.js">jQuery UI (js/jquery-ui-1.8.19.custom.min.js)</a>, and <a href="css/custom-theme/jquery-ui-1.8.19.custom.css">css/custom-theme/jquery-ui-1.8.19.custom.css</a> which imports the entire jQuery UI CSS Framework. You can choose to link a subset of the CSS Framework depending on your needs. </p>
	<p style="font-size: 1.2em; line-height: 1.5; margin: 1em 0; width: 50%;">You've downloaded components and a theme that are compatible with jQuery 1.3+. Please make sure you are using jQuery 1.3+ in your production environment.</p>

	<p style="font-weight: bold; margin: 2em 0 1em; font-size: 1.3em;">YOUR COMPONENTS:</p>


		<h2 class="demoHeaders">Framework Icons (content color preview)</h2>
		<ul id="icons" class="ui-widget ui-helper-clearfix">

		<li class="ui-state-default ui-corner-all" title=".ui-icon-carat-1-n"><span class="ui-icon ui-icon-carat-1-n"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-carat-1-ne"><span class="ui-icon ui-icon-carat-1-ne"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-carat-1-e"><span class="ui-icon ui-icon-carat-1-e"></span></li>

		<li class="ui-state-default ui-corner-all" title=".ui-icon-carat-1-se"><span class="ui-icon ui-icon-carat-1-se"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-carat-1-s"><span class="ui-icon ui-icon-carat-1-s"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-carat-1-sw"><span class="ui-icon ui-icon-carat-1-sw"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-carat-1-w"><span class="ui-icon ui-icon-carat-1-w"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-carat-1-nw"><span class="ui-icon ui-icon-carat-1-nw"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-carat-2-n-s"><span class="ui-icon ui-icon-carat-2-n-s"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-carat-2-e-w"><span class="ui-icon ui-icon-carat-2-e-w"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-triangle-1-n"><span class="ui-icon ui-icon-triangle-1-n"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-triangle-1-ne"><span class="ui-icon ui-icon-triangle-1-ne"></span></li>

		<li class="ui-state-default ui-corner-all" title=".ui-icon-triangle-1-e"><span class="ui-icon ui-icon-triangle-1-e"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-triangle-1-se"><span class="ui-icon ui-icon-triangle-1-se"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-triangle-1-s"><span class="ui-icon ui-icon-triangle-1-s"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-triangle-1-sw"><span class="ui-icon ui-icon-triangle-1-sw"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-triangle-1-w"><span class="ui-icon ui-icon-triangle-1-w"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-triangle-1-nw"><span class="ui-icon ui-icon-triangle-1-nw"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-triangle-2-n-s"><span class="ui-icon ui-icon-triangle-2-n-s"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-triangle-2-e-w"><span class="ui-icon ui-icon-triangle-2-e-w"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrow-1-n"><span class="ui-icon ui-icon-arrow-1-n"></span></li>

		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrow-1-ne"><span class="ui-icon ui-icon-arrow-1-ne"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrow-1-e"><span class="ui-icon ui-icon-arrow-1-e"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrow-1-se"><span class="ui-icon ui-icon-arrow-1-se"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrow-1-s"><span class="ui-icon ui-icon-arrow-1-s"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrow-1-sw"><span class="ui-icon ui-icon-arrow-1-sw"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrow-1-w"><span class="ui-icon ui-icon-arrow-1-w"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrow-1-nw"><span class="ui-icon ui-icon-arrow-1-nw"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrow-2-n-s"><span class="ui-icon ui-icon-arrow-2-n-s"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrow-2-ne-sw"><span class="ui-icon ui-icon-arrow-2-ne-sw"></span></li>

		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrow-2-e-w"><span class="ui-icon ui-icon-arrow-2-e-w"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrow-2-se-nw"><span class="ui-icon ui-icon-arrow-2-se-nw"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowstop-1-n"><span class="ui-icon ui-icon-arrowstop-1-n"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowstop-1-e"><span class="ui-icon ui-icon-arrowstop-1-e"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowstop-1-s"><span class="ui-icon ui-icon-arrowstop-1-s"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowstop-1-w"><span class="ui-icon ui-icon-arrowstop-1-w"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowthick-1-n"><span class="ui-icon ui-icon-arrowthick-1-n"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowthick-1-ne"><span class="ui-icon ui-icon-arrowthick-1-ne"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowthick-1-e"><span class="ui-icon ui-icon-arrowthick-1-e"></span></li>

		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowthick-1-se"><span class="ui-icon ui-icon-arrowthick-1-se"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowthick-1-s"><span class="ui-icon ui-icon-arrowthick-1-s"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowthick-1-sw"><span class="ui-icon ui-icon-arrowthick-1-sw"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowthick-1-w"><span class="ui-icon ui-icon-arrowthick-1-w"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowthick-1-nw"><span class="ui-icon ui-icon-arrowthick-1-nw"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowthick-2-n-s"><span class="ui-icon ui-icon-arrowthick-2-n-s"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowthick-2-ne-sw"><span class="ui-icon ui-icon-arrowthick-2-ne-sw"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowthick-2-e-w"><span class="ui-icon ui-icon-arrowthick-2-e-w"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowthick-2-se-nw"><span class="ui-icon ui-icon-arrowthick-2-se-nw"></span></li>

		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowthickstop-1-n"><span class="ui-icon ui-icon-arrowthickstop-1-n"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowthickstop-1-e"><span class="ui-icon ui-icon-arrowthickstop-1-e"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowthickstop-1-s"><span class="ui-icon ui-icon-arrowthickstop-1-s"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowthickstop-1-w"><span class="ui-icon ui-icon-arrowthickstop-1-w"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowreturnthick-1-w"><span class="ui-icon ui-icon-arrowreturnthick-1-w"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowreturnthick-1-n"><span class="ui-icon ui-icon-arrowreturnthick-1-n"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowreturnthick-1-e"><span class="ui-icon ui-icon-arrowreturnthick-1-e"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowreturnthick-1-s"><span class="ui-icon ui-icon-arrowreturnthick-1-s"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowreturn-1-w"><span class="ui-icon ui-icon-arrowreturn-1-w"></span></li>

		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowreturn-1-n"><span class="ui-icon ui-icon-arrowreturn-1-n"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowreturn-1-e"><span class="ui-icon ui-icon-arrowreturn-1-e"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowreturn-1-s"><span class="ui-icon ui-icon-arrowreturn-1-s"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowrefresh-1-w"><span class="ui-icon ui-icon-arrowrefresh-1-w"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowrefresh-1-n"><span class="ui-icon ui-icon-arrowrefresh-1-n"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowrefresh-1-e"><span class="ui-icon ui-icon-arrowrefresh-1-e"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrowrefresh-1-s"><span class="ui-icon ui-icon-arrowrefresh-1-s"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrow-4"><span class="ui-icon ui-icon-arrow-4"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-arrow-4-diag"><span class="ui-icon ui-icon-arrow-4-diag"></span></li>

		<li class="ui-state-default ui-corner-all" title=".ui-icon-extlink"><span class="ui-icon ui-icon-extlink"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-newwin"><span class="ui-icon ui-icon-newwin"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-refresh"><span class="ui-icon ui-icon-refresh"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-shuffle"><span class="ui-icon ui-icon-shuffle"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-transfer-e-w"><span class="ui-icon ui-icon-transfer-e-w"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-transferthick-e-w"><span class="ui-icon ui-icon-transferthick-e-w"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-folder-collapsed"><span class="ui-icon ui-icon-folder-collapsed"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-folder-open"><span class="ui-icon ui-icon-folder-open"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-document"><span class="ui-icon ui-icon-document"></span></li>

		<li class="ui-state-default ui-corner-all" title=".ui-icon-document-b"><span class="ui-icon ui-icon-document-b"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-note"><span class="ui-icon ui-icon-note"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-mail-closed"><span class="ui-icon ui-icon-mail-closed"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-mail-open"><span class="ui-icon ui-icon-mail-open"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-suitcase"><span class="ui-icon ui-icon-suitcase"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-comment"><span class="ui-icon ui-icon-comment"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-person"><span class="ui-icon ui-icon-person"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-print"><span class="ui-icon ui-icon-print"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-trash"><span class="ui-icon ui-icon-trash"></span></li>

		<li class="ui-state-default ui-corner-all" title=".ui-icon-locked"><span class="ui-icon ui-icon-locked"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-unlocked"><span class="ui-icon ui-icon-unlocked"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-bookmark"><span class="ui-icon ui-icon-bookmark"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-tag"><span class="ui-icon ui-icon-tag"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-home"><span class="ui-icon ui-icon-home"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-flag"><span class="ui-icon ui-icon-flag"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-calculator"><span class="ui-icon ui-icon-calculator"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-cart"><span class="ui-icon ui-icon-cart"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-pencil"><span class="ui-icon ui-icon-pencil"></span></li>

		<li class="ui-state-default ui-corner-all" title=".ui-icon-clock"><span class="ui-icon ui-icon-clock"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-disk"><span class="ui-icon ui-icon-disk"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-calendar"><span class="ui-icon ui-icon-calendar"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-zoomin"><span class="ui-icon ui-icon-zoomin"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-zoomout"><span class="ui-icon ui-icon-zoomout"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-search"><span class="ui-icon ui-icon-search"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-wrench"><span class="ui-icon ui-icon-wrench"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-gear"><span class="ui-icon ui-icon-gear"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-heart"><span class="ui-icon ui-icon-heart"></span></li>

		<li class="ui-state-default ui-corner-all" title=".ui-icon-star"><span class="ui-icon ui-icon-star"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-link"><span class="ui-icon ui-icon-link"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-cancel"><span class="ui-icon ui-icon-cancel"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-plus"><span class="ui-icon ui-icon-plus"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-plusthick"><span class="ui-icon ui-icon-plusthick"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-minus"><span class="ui-icon ui-icon-minus"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-minusthick"><span class="ui-icon ui-icon-minusthick"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-close"><span class="ui-icon ui-icon-close"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-closethick"><span class="ui-icon ui-icon-closethick"></span></li>

		<li class="ui-state-default ui-corner-all" title=".ui-icon-key"><span class="ui-icon ui-icon-key"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-lightbulb"><span class="ui-icon ui-icon-lightbulb"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-scissors"><span class="ui-icon ui-icon-scissors"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-clipboard"><span class="ui-icon ui-icon-clipboard"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-copy"><span class="ui-icon ui-icon-copy"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-contact"><span class="ui-icon ui-icon-contact"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-image"><span class="ui-icon ui-icon-image"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-video"><span class="ui-icon ui-icon-video"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-script"><span class="ui-icon ui-icon-script"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-alert"><span class="ui-icon ui-icon-alert"></span></li>

		<li class="ui-state-default ui-corner-all" title=".ui-icon-info"><span class="ui-icon ui-icon-info"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-notice"><span class="ui-icon ui-icon-notice"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-help"><span class="ui-icon ui-icon-help"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-check"><span class="ui-icon ui-icon-check"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-bullet"><span class="ui-icon ui-icon-bullet"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-radio-off"><span class="ui-icon ui-icon-radio-off"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-radio-on"><span class="ui-icon ui-icon-radio-on"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-pin-w"><span class="ui-icon ui-icon-pin-w"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-pin-s"><span class="ui-icon ui-icon-pin-s"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-play"><span class="ui-icon ui-icon-play"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-pause"><span class="ui-icon ui-icon-pause"></span></li>

		<li class="ui-state-default ui-corner-all" title=".ui-icon-seek-next"><span class="ui-icon ui-icon-seek-next"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-seek-prev"><span class="ui-icon ui-icon-seek-prev"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-seek-end"><span class="ui-icon ui-icon-seek-end"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-seek-first"><span class="ui-icon ui-icon-seek-first"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-stop"><span class="ui-icon ui-icon-stop"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-eject"><span class="ui-icon ui-icon-eject"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-volume-off"><span class="ui-icon ui-icon-volume-off"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-volume-on"><span class="ui-icon ui-icon-volume-on"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-power"><span class="ui-icon ui-icon-power"></span></li>

		<li class="ui-state-default ui-corner-all" title=".ui-icon-signal-diag"><span class="ui-icon ui-icon-signal-diag"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-signal"><span class="ui-icon ui-icon-signal"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-battery-0"><span class="ui-icon ui-icon-battery-0"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-battery-1"><span class="ui-icon ui-icon-battery-1"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-battery-2"><span class="ui-icon ui-icon-battery-2"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-battery-3"><span class="ui-icon ui-icon-battery-3"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-circle-plus"><span class="ui-icon ui-icon-circle-plus"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-circle-minus"><span class="ui-icon ui-icon-circle-minus"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-circle-close"><span class="ui-icon ui-icon-circle-close"></span></li>

		<li class="ui-state-default ui-corner-all" title=".ui-icon-circle-triangle-e"><span class="ui-icon ui-icon-circle-triangle-e"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-circle-triangle-s"><span class="ui-icon ui-icon-circle-triangle-s"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-circle-triangle-w"><span class="ui-icon ui-icon-circle-triangle-w"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-circle-triangle-n"><span class="ui-icon ui-icon-circle-triangle-n"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-circle-arrow-e"><span class="ui-icon ui-icon-circle-arrow-e"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-circle-arrow-s"><span class="ui-icon ui-icon-circle-arrow-s"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-circle-arrow-w"><span class="ui-icon ui-icon-circle-arrow-w"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-circle-arrow-n"><span class="ui-icon ui-icon-circle-arrow-n"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-circle-zoomin"><span class="ui-icon ui-icon-circle-zoomin"></span></li>

		<li class="ui-state-default ui-corner-all" title=".ui-icon-circle-zoomout"><span class="ui-icon ui-icon-circle-zoomout"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-circle-check"><span class="ui-icon ui-icon-circle-check"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-circlesmall-plus"><span class="ui-icon ui-icon-circlesmall-plus"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-circlesmall-minus"><span class="ui-icon ui-icon-circlesmall-minus"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-circlesmall-close"><span class="ui-icon ui-icon-circlesmall-close"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-squaresmall-plus"><span class="ui-icon ui-icon-squaresmall-plus"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-squaresmall-minus"><span class="ui-icon ui-icon-squaresmall-minus"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-squaresmall-close"><span class="ui-icon ui-icon-squaresmall-close"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-grip-dotted-vertical"><span class="ui-icon ui-icon-grip-dotted-vertical"></span></li>

		<li class="ui-state-default ui-corner-all" title=".ui-icon-grip-dotted-horizontal"><span class="ui-icon ui-icon-grip-dotted-horizontal"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-grip-solid-vertical"><span class="ui-icon ui-icon-grip-solid-vertical"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-grip-solid-horizontal"><span class="ui-icon ui-icon-grip-solid-horizontal"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-gripsmall-diagonal-se"><span class="ui-icon ui-icon-gripsmall-diagonal-se"></span></li>
		<li class="ui-state-default ui-corner-all" title=".ui-icon-grip-diagonal-se"><span class="ui-icon ui-icon-grip-diagonal-se"></span></li>
		</ul>


		<!-- Datepicker -->
		<h2 class="demoHeaders">Datepicker</h2>
		<div id="datepicker"></div>

		<!-- Highlight / Error -->
		<h2 class="demoHeaders">Highlight / Error</h2>
		<div class="ui-widget">
			<div class="ui-state-highlight ui-corner-all" style="margin-top: 20px; padding: 0 .7em;">
				<p><span class="ui-icon ui-icon-info" style="float: left; margin-right: .3em;"></span>
				<strong>Hey!</strong> Sample ui-state-highlight style.</p>
			</div>
		</div>
		<br/>
		<div class="ui-widget">
			<div class="ui-state-error ui-corner-all" style="padding: 0 .7em;">
				<p><span class="ui-icon ui-icon-alert" style="float: left; margin-right: .3em;"></span>
				<strong>Alert:</strong> Sample ui-state-error style.</p>
			</div>
		</div>

	</body>
</html>



```

## File: source\Conference\Conference.Web\Content\form\ui\css\custom-theme\jquery-ui-1.8.19.custom.css
```
/*!
 * jQuery UI CSS Framework 1.8.19
 *
 * Copyright 2012, AUTHORS.txt (http://jqueryui.com/about)
 * Dual licensed under the MIT or GPL Version 2 licenses.
 * http://jquery.org/license
 *
 * http://docs.jquery.com/UI/Theming/API
 */

/* Layout helpers
----------------------------------*/
.ui-helper-hidden { display: none; }
.ui-helper-hidden-accessible { position: absolute !important; clip: rect(1px 1px 1px 1px); clip: rect(1px,1px,1px,1px); }
.ui-helper-reset { margin: 0; padding: 0; border: 0; outline: 0; line-height: 1.3; text-decoration: none; font-size: 100%; list-style: none; }
.ui-helper-clearfix:before, .ui-helper-clearfix:after { content: ""; display: table; }
.ui-helper-clearfix:after { clear: both; }
.ui-helper-clearfix { zoom: 1; }
.ui-helper-zfix { width: 100%; height: 100%; top: 0; left: 0; position: absolute; opacity: 0; filter:Alpha(Opacity=0); }


/* Interaction Cues
----------------------------------*/
.ui-state-disabled { cursor: default !important; }


/* Icons
----------------------------------*/

/* states and images */
.ui-icon { display: block; text-indent: -99999px; overflow: hidden; background-repeat: no-repeat; }


/* Misc visuals
----------------------------------*/

/* Overlays */
.ui-widget-overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }


/*!
 * jQuery UI CSS Framework 1.8.19
 *
 * Copyright 2012, AUTHORS.txt (http://jqueryui.com/about)
 * Dual licensed under the MIT or GPL Version 2 licenses.
 * http://jquery.org/license
 *
 * http://docs.jquery.com/UI/Theming/API
 *
 * To view and modify this theme, visit http://jqueryui.com/themeroller/?ffDefault=Segoe%20UI,Arial,sans-serif&fwDefault=normal&fsDefault=11px&cornerRadius=0&bgColorHeader=2f7d00&bgTextureHeader=01_flat.png&bgImgOpacityHeader=100&borderColorHeader=2f7d00&fcHeader=ffffff&iconColorHeader=97be80&bgColorContent=2f7d00&bgTextureContent=01_flat.png&bgImgOpacityContent=100&borderColorContent=2f7d00&fcContent=ffffff&iconColorContent=97be80&bgColorDefault=2f7d00&bgTextureDefault=01_flat.png&bgImgOpacityDefault=100&borderColorDefault=2f7d00&fcDefault=ffffff&iconColorDefault=97be80&bgColorHover=599733&bgTextureHover=01_flat.png&bgImgOpacityHover=75&borderColorHover=599733&fcHover=ffffff&iconColorHover=97be80&bgColorActive=ffffff&bgTextureActive=02_glass.png&bgImgOpacityActive=65&borderColorActive=ffffff&fcActive=2f7d00&iconColorActive=97be80&bgColorHighlight=fbf9ee&bgTextureHighlight=02_glass.png&bgImgOpacityHighlight=55&borderColorHighlight=fcefa1&fcHighlight=363636&iconColorHighlight=2e83ff&bgColorError=fef1ec&bgTextureError=05_inset_soft.png&bgImgOpacityError=95&borderColorError=cd0a0a&fcError=cd0a0a&iconColorError=cd0a0a&bgColorOverlay=aaaaaa&bgTextureOverlay=01_flat.png&bgImgOpacityOverlay=0&opacityOverlay=30&bgColorShadow=aaaaaa&bgTextureShadow=01_flat.png&bgImgOpacityShadow=0&opacityShadow=30&thicknessShadow=8px&offsetTopShadow=-8px&offsetLeftShadow=-8px&cornerRadiusShadow=8px
 */


/* Component containers
----------------------------------*/
.ui-widget { font-family: Segoe UI,Arial,sans-serif; font-size: 11px; }
.ui-widget .ui-widget { font-size: 1em; }
.ui-widget input, .ui-widget select, .ui-widget textarea, .ui-widget button { font-family: Segoe UI,Arial,sans-serif; font-size: 1em; }
.ui-widget-content { border: 1px solid #2f7d00; background: #2f7d00 url(images/ui-bg_flat_100_2f7d00_40x100.png) 50% 50% repeat-x; color: #ffffff; }
.ui-widget-content a { color: #ffffff; }
.ui-widget-header { border: 1px solid #2f7d00; background: #2f7d00 url(images/ui-bg_flat_100_2f7d00_40x100.png) 50% 50% repeat-x; color: #ffffff; font-weight: bold; }
.ui-widget-header a { color: #ffffff; }

/* Interaction states
----------------------------------*/
.ui-state-default, .ui-widget-content .ui-state-default, .ui-widget-header .ui-state-default { border: 1px solid #2f7d00; background: #2f7d00 url(images/ui-bg_flat_100_2f7d00_40x100.png) 50% 50% repeat-x; font-weight: normal; color: #ffffff; }
.ui-state-default a, .ui-state-default a:link, .ui-state-default a:visited { color: #ffffff; text-decoration: none; }
.ui-state-hover, .ui-widget-content .ui-state-hover, .ui-widget-header .ui-state-hover, .ui-state-focus, .ui-widget-content .ui-state-focus, .ui-widget-header .ui-state-focus { border: 1px solid #599733; background: #599733 url(images/ui-bg_flat_75_599733_40x100.png) 50% 50% repeat-x; font-weight: normal; color: #ffffff; }
.ui-state-hover a, .ui-state-hover a:hover { color: #ffffff; text-decoration: none; }
.ui-state-active, .ui-widget-content .ui-state-active, .ui-widget-header .ui-state-active { border: 1px solid #ffffff; background: #ffffff url(images/ui-bg_glass_65_ffffff_1x400.png) 50% 50% repeat-x; font-weight: normal; color: #2f7d00; }
.ui-state-active a, .ui-state-active a:link, .ui-state-active a:visited { color: #2f7d00; text-decoration: none; }
.ui-widget :active { outline: none; }

/* Interaction Cues
----------------------------------*/
.ui-state-highlight, .ui-widget-content .ui-state-highlight, .ui-widget-header .ui-state-highlight  {border: 1px solid #40A800; background: #4BC400; color: #363636; }
.ui-state-highlight a, .ui-widget-content .ui-state-highlight a,.ui-widget-header .ui-state-highlight a { color: #363636; }
.ui-state-error, .ui-widget-content .ui-state-error, .ui-widget-header .ui-state-error {border: 1px solid #cd0a0a; background: #fef1ec url(images/ui-bg_inset-soft_95_fef1ec_1x100.png) 50% bottom repeat-x; color: #cd0a0a; }
.ui-state-error a, .ui-widget-content .ui-state-error a, .ui-widget-header .ui-state-error a { color: #cd0a0a; }
.ui-state-error-text, .ui-widget-content .ui-state-error-text, .ui-widget-header .ui-state-error-text { color: #cd0a0a; }
.ui-priority-primary, .ui-widget-content .ui-priority-primary, .ui-widget-header .ui-priority-primary { font-weight: bold; }
.ui-priority-secondary, .ui-widget-content .ui-priority-secondary,  .ui-widget-header .ui-priority-secondary { opacity: .7; filter:Alpha(Opacity=70); font-weight: normal; }
/*.ui-state-disabled, .ui-widget-content .ui-state-disabled, .ui-widget-header .ui-state-disabled { opacity: .35; filter:Alpha(Opacity=35); background-image: none; }*/

/* Icons
----------------------------------*/

/* states and images */
.ui-icon { width: 16px; height: 16px; background-image: url(images/ui-icons_97be80_256x240.png); }
.ui-widget-content .ui-icon {background-image: url(images/ui-icons_97be80_256x240.png); }
.ui-widget-header .ui-icon {background-image: url(images/ui-icons_97be80_256x240.png); }
.ui-state-default .ui-icon { background-image: url(images/ui-icons_97be80_256x240.png); }
.ui-state-hover .ui-icon, .ui-state-focus .ui-icon {background-image: url(images/ui-icons_97be80_256x240.png); }
.ui-state-active .ui-icon {background-image: url(images/ui-icons_97be80_256x240.png); }
.ui-state-highlight .ui-icon {background-image: url(images/ui-icons_2e83ff_256x240.png); }
.ui-state-error .ui-icon, .ui-state-error-text .ui-icon {background-image: url(images/ui-icons_cd0a0a_256x240.png); }

/* positioning */
.ui-icon-carat-1-n { background-position: 0 0; }
.ui-icon-carat-1-ne { background-position: -16px 0; }
.ui-icon-carat-1-e { background-position: -32px 0; }
.ui-icon-carat-1-se { background-position: -48px 0; }
.ui-icon-carat-1-s { background-position: -64px 0; }
.ui-icon-carat-1-sw { background-position: -80px 0; }
.ui-icon-carat-1-w { background-position: -96px 0; }
.ui-icon-carat-1-nw { background-position: -112px 0; }
.ui-icon-carat-2-n-s { background-position: -128px 0; }
.ui-icon-carat-2-e-w { background-position: -144px 0; }
.ui-icon-triangle-1-n { background-position: 0 -16px; }
.ui-icon-triangle-1-ne { background-position: -16px -16px; }
.ui-icon-triangle-1-e { background-position: -32px -16px; }
.ui-icon-triangle-1-se { background-position: -48px -16px; }
.ui-icon-triangle-1-s { background-position: -64px -16px; }
.ui-icon-triangle-1-sw { background-position: -80px -16px; }
.ui-icon-triangle-1-w { background-position: -96px -16px; }
.ui-icon-triangle-1-nw { background-position: -112px -16px; }
.ui-icon-triangle-2-n-s { background-position: -128px -16px; }
.ui-icon-triangle-2-e-w { background-position: -144px -16px; }
.ui-icon-arrow-1-n { background-position: 0 -32px; }
.ui-icon-arrow-1-ne { background-position: -16px -32px; }
.ui-icon-arrow-1-e { background-position: -32px -32px; }
.ui-icon-arrow-1-se { background-position: -48px -32px; }
.ui-icon-arrow-1-s { background-position: -64px -32px; }
.ui-icon-arrow-1-sw { background-position: -80px -32px; }
.ui-icon-arrow-1-w { background-position: -96px -32px; }
.ui-icon-arrow-1-nw { background-position: -112px -32px; }
.ui-icon-arrow-2-n-s { background-position: -128px -32px; }
.ui-icon-arrow-2-ne-sw { background-position: -144px -32px; }
.ui-icon-arrow-2-e-w { background-position: -160px -32px; }
.ui-icon-arrow-2-se-nw { background-position: -176px -32px; }
.ui-icon-arrowstop-1-n { background-position: -192px -32px; }
.ui-icon-arrowstop-1-e { background-position: -208px -32px; }
.ui-icon-arrowstop-1-s { background-position: -224px -32px; }
.ui-icon-arrowstop-1-w { background-position: -240px -32px; }
.ui-icon-arrowthick-1-n { background-position: 0 -48px; }
.ui-icon-arrowthick-1-ne { background-position: -16px -48px; }
.ui-icon-arrowthick-1-e { background-position: -32px -48px; }
.ui-icon-arrowthick-1-se { background-position: -48px -48px; }
.ui-icon-arrowthick-1-s { background-position: -64px -48px; }
.ui-icon-arrowthick-1-sw { background-position: -80px -48px; }
.ui-icon-arrowthick-1-w { background-position: -96px -48px; }
.ui-icon-arrowthick-1-nw { background-position: -112px -48px; }
.ui-icon-arrowthick-2-n-s { background-position: -128px -48px; }
.ui-icon-arrowthick-2-ne-sw { background-position: -144px -48px; }
.ui-icon-arrowthick-2-e-w { background-position: -160px -48px; }
.ui-icon-arrowthick-2-se-nw { background-position: -176px -48px; }
.ui-icon-arrowthickstop-1-n { background-position: -192px -48px; }
.ui-icon-arrowthickstop-1-e { background-position: -208px -48px; }
.ui-icon-arrowthickstop-1-s { background-position: -224px -48px; }
.ui-icon-arrowthickstop-1-w { background-position: -240px -48px; }
.ui-icon-arrowreturnthick-1-w { background-position: 0 -64px; }
.ui-icon-arrowreturnthick-1-n { background-position: -16px -64px; }
.ui-icon-arrowreturnthick-1-e { background-position: -32px -64px; }
.ui-icon-arrowreturnthick-1-s { background-position: -48px -64px; }
.ui-icon-arrowreturn-1-w { background-position: -64px -64px; }
.ui-icon-arrowreturn-1-n { background-position: -80px -64px; }
.ui-icon-arrowreturn-1-e { background-position: -96px -64px; }
.ui-icon-arrowreturn-1-s { background-position: -112px -64px; }
.ui-icon-arrowrefresh-1-w { background-position: -128px -64px; }
.ui-icon-arrowrefresh-1-n { background-position: -144px -64px; }
.ui-icon-arrowrefresh-1-e { background-position: -160px -64px; }
.ui-icon-arrowrefresh-1-s { background-position: -176px -64px; }
.ui-icon-arrow-4 { background-position: 0 -80px; }
.ui-icon-arrow-4-diag { background-position: -16px -80px; }
.ui-icon-extlink { background-position: -32px -80px; }
.ui-icon-newwin { background-position: -48px -80px; }
.ui-icon-refresh { background-position: -64px -80px; }
.ui-icon-shuffle { background-position: -80px -80px; }
.ui-icon-transfer-e-w { background-position: -96px -80px; }
.ui-icon-transferthick-e-w { background-position: -112px -80px; }
.ui-icon-folder-collapsed { background-position: 0 -96px; }
.ui-icon-folder-open { background-position: -16px -96px; }
.ui-icon-document { background-position: -32px -96px; }
.ui-icon-document-b { background-position: -48px -96px; }
.ui-icon-note { background-position: -64px -96px; }
.ui-icon-mail-closed { background-position: -80px -96px; }
.ui-icon-mail-open { background-position: -96px -96px; }
.ui-icon-suitcase { background-position: -112px -96px; }
.ui-icon-comment { background-position: -128px -96px; }
.ui-icon-person { background-position: -144px -96px; }
.ui-icon-print { background-position: -160px -96px; }
.ui-icon-trash { background-position: -176px -96px; }
.ui-icon-locked { background-position: -192px -96px; }
.ui-icon-unlocked { background-position: -208px -96px; }
.ui-icon-bookmark { background-position: -224px -96px; }
.ui-icon-tag { background-position: -240px -96px; }
.ui-icon-home { background-position: 0 -112px; }
.ui-icon-flag { background-position: -16px -112px; }
.ui-icon-calendar { background-position: -32px -112px; }
.ui-icon-cart { background-position: -48px -112px; }
.ui-icon-pencil { background-position: -64px -112px; }
.ui-icon-clock { background-position: -80px -112px; }
.ui-icon-disk { background-position: -96px -112px; }
.ui-icon-calculator { background-position: -112px -112px; }
.ui-icon-zoomin { background-position: -128px -112px; }
.ui-icon-zoomout { background-position: -144px -112px; }
.ui-icon-search { background-position: -160px -112px; }
.ui-icon-wrench { background-position: -176px -112px; }
.ui-icon-gear { background-position: -192px -112px; }
.ui-icon-heart { background-position: -208px -112px; }
.ui-icon-star { background-position: -224px -112px; }
.ui-icon-link { background-position: -240px -112px; }
.ui-icon-cancel { background-position: 0 -128px; }
.ui-icon-plus { background-position: -16px -128px; }
.ui-icon-plusthick { background-position: -32px -128px; }
.ui-icon-minus { background-position: -48px -128px; }
.ui-icon-minusthick { background-position: -64px -128px; }
.ui-icon-close { background-position: -80px -128px; }
.ui-icon-closethick { background-position: -96px -128px; }
.ui-icon-key { background-position: -112px -128px; }
.ui-icon-lightbulb { background-position: -128px -128px; }
.ui-icon-scissors { background-position: -144px -128px; }
.ui-icon-clipboard { background-position: -160px -128px; }
.ui-icon-copy { background-position: -176px -128px; }
.ui-icon-contact { background-position: -192px -128px; }
.ui-icon-image { background-position: -208px -128px; }
.ui-icon-video { background-position: -224px -128px; }
.ui-icon-script { background-position: -240px -128px; }
.ui-icon-alert { background-position: 0 -144px; }
.ui-icon-info { background-position: -16px -144px; }
.ui-icon-notice { background-position: -32px -144px; }
.ui-icon-help { background-position: -48px -144px; }
.ui-icon-check { background-position: -64px -144px; }
.ui-icon-bullet { background-position: -80px -144px; }
.ui-icon-radio-off { background-position: -96px -144px; }
.ui-icon-radio-on { background-position: -112px -144px; }
.ui-icon-pin-w { background-position: -128px -144px; }
.ui-icon-pin-s { background-position: -144px -144px; }
.ui-icon-play { background-position: 0 -160px; }
.ui-icon-pause { background-position: -16px -160px; }
.ui-icon-seek-next { background-position: -32px -160px; }
.ui-icon-seek-prev { background-position: -48px -160px; }
.ui-icon-seek-end { background-position: -64px -160px; }
.ui-icon-seek-start { background-position: -80px -160px; }
/* ui-icon-seek-first is deprecated, use ui-icon-seek-start instead */
.ui-icon-seek-first { background-position: -80px -160px; }
.ui-icon-stop { background-position: -96px -160px; }
.ui-icon-eject { background-position: -112px -160px; }
.ui-icon-volume-off { background-position: -128px -160px; }
.ui-icon-volume-on { background-position: -144px -160px; }
.ui-icon-power { background-position: 0 -176px; }
.ui-icon-signal-diag { background-position: -16px -176px; }
.ui-icon-signal { background-position: -32px -176px; }
.ui-icon-battery-0 { background-position: -48px -176px; }
.ui-icon-battery-1 { background-position: -64px -176px; }
.ui-icon-battery-2 { background-position: -80px -176px; }
.ui-icon-battery-3 { background-position: -96px -176px; }
.ui-icon-circle-plus { background-position: 0 -192px; }
.ui-icon-circle-minus { background-position: -16px -192px; }
.ui-icon-circle-close { background-position: -32px -192px; }
.ui-icon-circle-triangle-e { background-position: -48px -192px; }
.ui-icon-circle-triangle-s { background-position: -64px -192px; }
.ui-icon-circle-triangle-w { background-position: -80px -192px; }
.ui-icon-circle-triangle-n { background-position: -96px -192px; }
.ui-icon-circle-arrow-e { background-position: -112px -192px; }
.ui-icon-circle-arrow-s { background-position: -128px -192px; }
.ui-icon-circle-arrow-w { background-position: -144px -192px; }
.ui-icon-circle-arrow-n { background-position: -160px -192px; }
.ui-icon-circle-zoomin { background-position: -176px -192px; }
.ui-icon-circle-zoomout { background-position: -192px -192px; }
.ui-icon-circle-check { background-position: -208px -192px; }
.ui-icon-circlesmall-plus { background-position: 0 -208px; }
.ui-icon-circlesmall-minus { background-position: -16px -208px; }
.ui-icon-circlesmall-close { background-position: -32px -208px; }
.ui-icon-squaresmall-plus { background-position: -48px -208px; }
.ui-icon-squaresmall-minus { background-position: -64px -208px; }
.ui-icon-squaresmall-close { background-position: -80px -208px; }
.ui-icon-grip-dotted-vertical { background-position: 0 -224px; }
.ui-icon-grip-dotted-horizontal { background-position: -16px -224px; }
.ui-icon-grip-solid-vertical { background-position: -32px -224px; }
.ui-icon-grip-solid-horizontal { background-position: -48px -224px; }
.ui-icon-gripsmall-diagonal-se { background-position: -64px -224px; }
.ui-icon-grip-diagonal-se { background-position: -80px -224px; }


/* Misc visuals
----------------------------------*/

/* Corner radius */
.ui-corner-all, .ui-corner-top, .ui-corner-left, .ui-corner-tl { -moz-border-radius-topleft: 0; -webkit-border-top-left-radius: 0; -khtml-border-top-left-radius: 0; border-top-left-radius: 0; }
.ui-corner-all, .ui-corner-top, .ui-corner-right, .ui-corner-tr { -moz-border-radius-topright: 0; -webkit-border-top-right-radius: 0; -khtml-border-top-right-radius: 0; border-top-right-radius: 0; }
.ui-corner-all, .ui-corner-bottom, .ui-corner-left, .ui-corner-bl { -moz-border-radius-bottomleft: 0; -webkit-border-bottom-left-radius: 0; -khtml-border-bottom-left-radius: 0; border-bottom-left-radius: 0; }
.ui-corner-all, .ui-corner-bottom, .ui-corner-right, .ui-corner-br { -moz-border-radius-bottomright: 0; -webkit-border-bottom-right-radius: 0; -khtml-border-bottom-right-radius: 0; border-bottom-right-radius: 0; }

/* Overlays */
.ui-widget-overlay { background: #aaaaaa url(images/ui-bg_flat_0_aaaaaa_40x100.png) 50% 50% repeat-x; opacity: .30;filter:Alpha(Opacity=30); }
.ui-widget-shadow { margin: -8px 0 0 -8px; padding: 8px; background: #aaaaaa url(images/ui-bg_flat_0_aaaaaa_40x100.png) 50% 50% repeat-x; opacity: .30;filter:Alpha(Opacity=30); -moz-border-radius: 8px; -khtml-border-radius: 8px; -webkit-border-radius: 8px; border-radius: 8px; }/*!
 * jQuery UI Datepicker 1.8.19
 *
 * Copyright 2012, AUTHORS.txt (http://jqueryui.com/about)
 * Dual licensed under the MIT or GPL Version 2 licenses.
 * http://jquery.org/license
 *
 * http://docs.jquery.com/UI/Datepicker#theming
 */
.ui-datepicker { width: 17em; padding: 10px .2em 0; display: none; }
.ui-datepicker .ui-datepicker-header { position:relative; padding: 0 0; }
.ui-datepicker .ui-datepicker-prev, .ui-datepicker .ui-datepicker-next { position:absolute; top: 0; width: 24px; height: 24px; cursor: pointer;}
.ui-datepicker .ui-datepicker-prev-hover, .ui-datepicker .ui-datepicker-next-hover { top: 0; }
.ui-datepicker .ui-datepicker-prev { left: 0;
	}
.ui-datepicker .ui-datepicker-prev:hover,.ui-datepicker .ui-datepicker-next:hover {
	border: none!important;
	}
.ui-datepicker .ui-datepicker-next { right:0; }
.ui-datepicker .ui-datepicker-prev-hover { left: 0; }
.ui-datepicker .ui-datepicker-next-hover { right: 0; }
.ui-datepicker .ui-datepicker-prev span, .ui-datepicker .ui-datepicker-next span { display: block; width: 24px; height: 24px;  }
.ui-datepicker .ui-datepicker-prev span {
	background: url(images/ll.gif) left top no-repeat;
	width: 24px; height: 24px;
	}
.ui-datepicker .ui-datepicker-next span {
	background: url(images/rr.gif) left top no-repeat;
	width: 24px; height: 24px;
	}
.ui-datepicker .ui-datepicker-prev:hover span {
	background: url(images/l.gif) left top no-repeat;
	width: 24px; height: 24px;
	}
.ui-datepicker .ui-datepicker-next:hover span {
	background: url(images/r.gif) left top no-repeat;
	width: 24px; height: 24px;
	}
.ui-datepicker .ui-datepicker-title { margin: 0 30px; line-height: 1.8em; text-align: center; 
	font-size: 15px;
	font-family: Segoe UI;
	font-weight: normal;
	}
.ui-datepicker .ui-datepicker-title select { font-size:1em; margin: 1px 0; }
.ui-datepicker select.ui-datepicker-month-year {width: 100%;}
.ui-datepicker select.ui-datepicker-month, 
.ui-datepicker select.ui-datepicker-year { width: 49%;}
.ui-datepicker table {
	width: 100%; font-size: .9em; border-collapse: collapse; margin:0 0 .4em;
	border: none;
	border-spacing: 0;
	}
.ui-datepicker th { padding: .7em 0 8px; text-align: center; font-weight: normal; border: 0; 
	background: none;
	}
.ui-datepicker th  span {
	display: block;
	text-align: center;
	border-bottom: solid 1px #fff;
	padding: 0 0 8px;
	}
.ui-datepicker td { border: 0; padding: 0; border-spacing: 0; background: none;
	text-align: center;
	font-size: 11px;

	}
.ui-datepicker td span, .ui-datepicker td a { display: block; padding: .2em; text-align: center; text-decoration: none; }
.ui-datepicker .ui-datepicker-buttonpane { background-image: none; margin: .7em 0 0 0; padding:0 .2em; border-left: 0; border-right: 0; border-bottom: 0; }
.ui-datepicker .ui-datepicker-buttonpane button { float: right; margin: .5em .2em .4em; cursor: pointer; padding: .2em .6em .3em .6em; width:auto; overflow:visible; }
.ui-datepicker .ui-datepicker-buttonpane button.ui-datepicker-current { float:left; }

/* with multiple calendars */
.ui-datepicker.ui-datepicker-multi { width:auto; }
.ui-datepicker-multi .ui-datepicker-group { float:left; }
.ui-datepicker-multi .ui-datepicker-group table { width:95%; margin:0 auto .4em; }
.ui-datepicker-multi-2 .ui-datepicker-group { width:50%; }
.ui-datepicker-multi-3 .ui-datepicker-group { width:33.3%; }
.ui-datepicker-multi-4 .ui-datepicker-group { width:25%; }
.ui-datepicker-multi .ui-datepicker-group-last .ui-datepicker-header { border-left-width:0; }
.ui-datepicker-multi .ui-datepicker-group-middle .ui-datepicker-header { border-left-width:0; }
.ui-datepicker-multi .ui-datepicker-buttonpane { clear:left; }
.ui-datepicker-row-break { clear:both; width:100%; font-size:0em; }

/* RTL support */
.ui-datepicker-rtl { direction: rtl; }
.ui-datepicker-rtl .ui-datepicker-prev { right: 2px; left: auto; }
.ui-datepicker-rtl .ui-datepicker-next { left: 2px; right: auto; }
.ui-datepicker-rtl .ui-datepicker-prev:hover { right: 1px; left: auto; }
.ui-datepicker-rtl .ui-datepicker-next:hover { left: 1px; right: auto; }
.ui-datepicker-rtl .ui-datepicker-buttonpane { clear:right; }
.ui-datepicker-rtl .ui-datepicker-buttonpane button { float: left; }
.ui-datepicker-rtl .ui-datepicker-buttonpane button.ui-datepicker-current { float:right; }
.ui-datepicker-rtl .ui-datepicker-group { float:right; }
.ui-datepicker-rtl .ui-datepicker-group-last .ui-datepicker-header { border-right-width:0; border-left-width:1px; }
.ui-datepicker-rtl .ui-datepicker-group-middle .ui-datepicker-header { border-right-width:0; border-left-width:1px; }

/* IE6 IFRAME FIX (taken from datepicker 1.5.3 */
.ui-datepicker-cover {
    display: none; /*sorry for IE5*/
    display/**/: block; /*sorry for IE5*/
    position: absolute; /*must have*/
    z-index: -1; /*must have*/
    filter: mask(); /*must have*/
    top: -4px; /*must have*/
    left: -4px; /*must have*/
    width: 200px; /*must have*/
    height: 200px; /*must have*/
}
```

## File: source\Conference\Conference.Web\Content\likes\likes.css
```
.likes {}
.likes__link {
    margin-left: 10px;
    display: inline-block;
    width: 21px;
    height: 21px;
    background: url(likes_sprite.png);
}
*:first-child+html .likes__link {
    display: inline;
    zoom:1;
}
.likes__link_facebook {
    background-position: 0 0;
}
.likes__link_mail {
    background-position: -21px 0;
}
.likes__link_twitter {
    background-position: -42px 0;
}
```

## File: source\Conference\Conference.Web\Content\menu\menu.css
```
.menu {
}
.menu__list {
    overflow: hidden;
    padding-top: 8px;
    }
.menu__item {
    float: left;
    margin-right: 23px;
    }
    .menu__item_active, .menu__item_active a {
        font-weight: bold;
        color: #fff;
        }
.menu__item a {
    color: #cccccc;
    text-decoration: none;
    }
.menu__item a:hover {
	color: #66ccff;
	}
.menu__back {
    width: 32px;
    display: inline-block;
    height: 32px;
    background: url(menu__back.png);
    margin-right: 5px;
    position: relative;
    top: -8px;
    }
```

## File: source\Conference\Conference.Web\Content\nav\nav.css
```
.nav {
    overflow: hidden;
    font-family: "Segoe UI light";
    font-size: 36px;
	padding: 20px 0 0 0;
}
.nav__left,
.nav__right {
    min-height: 40px;
    text-decoration: none;
    line-height: 28px;
    padding-bottom: 9px;
	border: none;
	font-family: "Segoe UI light";
    font-size: 36px;
}
.nav__left {
    background:no-repeat left 1px url(nav__left.png);
    padding-left: 48px;
    float: left;
    color: #0099ff;
	text-align: right;
}
.nav__left:hover {
	background:no-repeat left 1px url(nav__left_a.png);
	color: #33ccff;
	}
.nav__right {
    background:no-repeat right 1px url(nav__right.png);
    padding-right: 48px;
    float: right;
    color: #ff9900;
	text-align: right;
	}
.nav__right:hover {
    background:no-repeat right 1px url(nav__right_a.png);
	color: #ffcc33;
	}
.nav__right-small {
    text-decoration: none;
	font-size: 13px;
	display: block;
	margin: 5px 0 0 0;
	}
```

## File: source\Conference\Conference.Web\Content\page\page.css
```
.page {
    min-height: 100%;
    color: #fff;
    background: #183b56;
}
.page_green {
	background: #0b3500;
	}
.page_green nav {
	background: #000;
	}
.page__wrapper {
    width: 1130px;
    margin: 0 auto;
}
.page_conference-seats .page__wrapper,
.page_create-conf .page__wrapper,
.page_registration .page__wrapper {
    width: 1070px;
    padding-left: 60px;
}
.page_conference .page__wrapper {
	width: 1130px;
	padding-left: 0;
}
nav {
    height: 22px;
    background: #0e2d44;
    padding-top: 4px;
}
.page_conference-seats nav .page__wrapper,
.page_create-conf nav .page__wrapper {
	width: 1130px;
    margin: 0 auto;
	padding-left: 0;
	}
.page__head {
    padding-top: 37px;
    padding-bottom: 13px;
    overflow: hidden;
    position: relative;
    left: -2px;
    min-height: 75px;
    font-size: 45px;
    font-family: "Segoe UI light", Arial, sans-serif;
    line-height: 32px;
    }
    .page__head-note {
        font-size: 28px;
        }
.page__content {}

.page__likes {
    margin-top: 20px;
    }
    .page__likes .page__wrapper {
        width: 943px;
        padding-right: 187px;
        text-align: right;
    }
.page__menu {
    margin: 23px auto -10px;
    width: 1130px;
}

div.lightbox {
	display: none;
	}
.lightbox-bg {
	background: #000; 
	opacity: 0.75; filter: alpha(opacity: 75); 
	position: fixed; left: 0; top: 0; _position: absolute; _top: expression(parseInt(document.body.scrollTop) + "px");
	width: 100%; height: 100%; }
table.lightbox {
	position: fixed; left: 0; top: 0; _position: absolute; _top: expression(parseInt(document.body.scrollTop) + "px");
	width: 100%; height: 100%; }
td.lightbox {
	text-align: center;
	vertical-align: middle;
	}
.lightbox-content {
	position: relative;
	display: inline-block;
	text-align: left;
	background: #fff; }
.lightbox-content_delete {
	background: #ffcc00 url(lightbox-content_delete.gif) 20px 20px no-repeat;
	width: 248px;
	padding: 0 30px 30px 85px;
	}
.lightbox-content__title {
	font-size: 36px;
	color: #333333;
	font-family: Segoe UI Light;
	line-height: 35px;
	padding: 24px 0 0;
	letter-spacing: -1px;
	}
.lightbox-content_delete__q {
	font-size: 15px;
	color: #333333;
	padding: 30px 0 0;
	}
.lightbox-content_delete__action {
	padding: 26px 0 0;
	}
.lightbox-content_delete__action__no,.lightbox-content_delete__action__no:active,.lightbox-content_delete__action__no:visited,.lightbox-content_delete__action__no:hover {
	display: inline-block;
	width: 60px; height: 40px;
	line-height: 40px;
	color: #ffffff;
	font-size: 15px;
	text-align: center;
	text-decoration: none;
	padding: 0 34px 0 0;
	background: #ff6600 url(lightbox-content_delete__action__no.gif) 60px 8px no-repeat;
	}
.lightbox-content_delete__action__yes,.lightbox-content_delete__action__yes:active,.lightbox-content_delete__action__yes:visited,.lightbox-content_delete__action__yes:hover {
	display: inline-block;
	margin: 0 0 0 30px;
	width: 60px; height: 40px;
	line-height: 40px;
	color: #ffffff;
	font-size: 15px;
	text-align: center;
	text-decoration: none;
	padding: 0 34px 0 0;
	background: #ff6600 url(lightbox-content_delete__action__yes.gif) 60px 8px no-repeat;
	}

```

## File: source\Conference\Conference.Web\Content\quick\quick.css
```
.quick {
    color: #cccccc;
    font-size: 11px;
    overflow: hidden;
}
.quick__list {
    float: left;
}
.quick__item {
    float: left;
    margin-right: 18px;
}
.quick__item a {
    color: #cccccc;
    text-decoration: none;
}
.quick__item a:hover {
	color: #66ccff;
	}
.quick__login {
    float: right;
    color: #cccccc;
    text-decoration: none;
}
.quick__item_bold a {
    font-weight: bold;
}

```

## File: source\Conference\Conference.Web\Content\table\table.css
```

```

## File: source\Conference\Conference.Web\Content\tabs\tabs.css
```
.tabs {
	margin: 0; padding: 0;
	}
.tabs__item {
	font-size: 28px;
	font-family: "Segoe UI light", "Arial", sans-serif;
	display: inline;
	margin: 0 30px 0 0;
	padding: 0;
	}
.tabs__item a,.tabs__item a:active,.tabs__item a:visited,.tabs__item a:hover {
	text-decoration: none;
	color: #859a80;
	}
.tabs__item a:hover {
	color: #66ccff;
	}
.tabs__item_active a,.tabs__item_active a:active,.tabs__item_active a:visited,.tabs__item_active a:hover {
	text-decoration: none;
	color: #fff;
	cursor: default;
	}
```

## File: source\Conference\Conference.Web\Content\tabs\tabs.js
```
$(function() {
	$('.js-reg-form').click(function(){
		$('.tabs__item').removeClass('tabs__item_active');
		$(this).addClass('tabs__item_active');
		
		$('.content').hide();
		$('.content_reg').show();
		return false;
	});
	$('.js-login-form').click(function(){
		$('.tabs__item').removeClass('tabs__item_active');
		$(this).addClass('tabs__item_active');
		
		$('.content').hide();
		$('.content_login').show();
		return false;
	});
});
```

## File: source\Conference\Conference.Web\Content\tile\tile.css
```
.tile {
    width: 240px;
    height: 140px;
    background: #2f7d00;
    position: relative;
    cursor: pointer;
    float: left;
    margin: 0 10px 10px 0;
    text-decoration: none;
	overflow: hidden;
}
.tile:hover {
	margin: -5px 5px 5px -5px;
	padding: 5px 5px 5px 5px;
	color: #fff;
	}
.tile__imgs {
	position: relative;
	margin: -5px 0 0 -5px;
	}
.tile__img {
	position: absolute;
	left: 0;
	top: 0;
	/*margin: -5px 0 0 -5px;*/
	}
.tile:hover .tile__img img {
	/*margin: 0;*/
	}
.tile__imgs {
	display: block;
	}
.tile__header {
    position: absolute;
    bottom: 0;
    padding-bottom: 3px;
    left: 0;
    font-size: 18px;
    line-height: 1;
    height: 18px;
    display: block;
	background: url(tile__header.png) repeat;
	width: 100%;
	padding: 5px 0 8px 10px;
	z-index: 50;
}
.tile:hover .tile__header {
	padding: 10px 0 13px 15px;
	}
.tile__img-container {
    margin-top: 20px;
    min-height: 68px;
    text-align: center;
    line-height: 68px;
    vertical-align: middle;
    display: block;
}


.tile__img-container img {
    vertical-align: middle;
}

.tile_narrow {
    width: 140px;
}
.tile_small {
    width: 128px;
    height: 40px;
    margin: 0;
    padding: 0;
}
.tile_small:hover {
	margin: -5px -5px 0 0;
	padding: 5px 5px 5px 5px;
	}
.tile_small .tile__header {
    font-size: 13px;
    line-height: 14px;
    font-family: "Segoe UI", Arial, sans-serif;
    position: static;
    overflow: hidden;
    height: auto;
    padding: 5px 0 0 0;
	width: auto;
}
.tile_small:hover .tile__header {
	padding: 5px 0 0 0;
	}
.tile_small img {
    float: left;
    margin: 11px 21px 11px 11px;
}


.tile_twitter {
    background: #0099cc;
    padding-left: 11px;
    padding-top: 5px;
    padding-right: 20px;
    width: 209px;
    height: 135px;
}
.tile_twitter:hover {
	margin: -5px 5px 5px -5px;
	padding: 10px 25px 5px 16px;
	}
.tile_twitter .tile__header {
    position: static;
    overflow: hidden;
    background:no-repeat left 5px url(tile_twitter.png);
    height: 30px;
    padding: 0 0 0 32px;
    font-size: 24px;
    line-height: 1;
    font-family: "Segoe UI light", Arial, sans-serif;
	width: auto;
}
.tile_twitter:hover .tile__header {
	padding: 0 0 0 32px;
	}
.tile__tweet,
.tile__twit {
    font-size: 13px;
    position: absolute;
    bottom: 9px;
    overflow: hidden;
    right: 20px;
    left: 11px;
    top: 50px;
    line-height: 16px;
    }
.tile_twitter:hover .tile__tweet {
	top: 55px;
	bottom: 14px;
	left: 16px;
	right: 25px;
	}
    .tile__nick {
        overflow: hidden;
        padding-right: 65px;
        font-size: 13px;
        font-weight: bold;
        line-height: 1;
        padding-bottom: 3px;
        display: block;
        }
        .tile__time {
            float: right;
            width: 65px;
            overflow: hidden;
            font-size: 11px;
            line-height: 1;
            height: 13px;
            text-align: right;
            margin-right: -65px;
        }
.tile_twitter .tile-slide{
	width: 209px;
	height:105px;
	position: relative;
	display: block;
	}
.tile-slide .tile__tweet {
	width: 209px;
	height: 81px;
	
	font-size: 13px;
    position: absolute;
    bottom: auto;
    overflow: hidden;
    right: 20px;
    left: 11px;
    top: 50px;
    line-height: 16px;
	padding: 10px 0 0;
	}


.tile_event {}
.tile__topic {
    font-weight: bold;
    line-height: 18px;
    padding-left: 10px;
    padding-top: 16px;
    display: block;
}
.tile__span {
    font-size: 11px;
    line-height: 1;
    padding-left: 10px;
    padding-top: 10px;
    display: block;
}
.tile__nav {
    display: inline-block;
    margin-left: 14px;
}
.tile__nav-item {
    margin-right: 5px;
    display: inline-block;
    text-decoration: none;
    border: 1px solid transparent;
    font: 0/0 Arial;
}
.tile__nav-item_active,
.tile__nav-item:hover {
    border-color: #fff;
}
.tile__nav-item i {
    font: 0/0 Arial;
    display: inline-block;
    width: 5px;
    height: 5px;
    background: #fff;
    margin: 1px;
}


.tile_register {
    background: #ff6600;
}
.tile_register .tile__header {
    margin: 0;
    padding: 16px 46px 5px 7px;
    position: static;
    font-size: 36px;
    line-height: 1;
    height: 36px;
    font-family: "Segoe UI light", Arial, sans-serif;
    display: inline-block;
    background: 100% 21px url(tile_register.png) no-repeat;
	width: auto;
}
.tile_register:hover .tile__header {
	padding: 16px 46px 5px 7px;
	}
.tile__note {
    line-height: 20px;
    padding-left: 10px;
    padding-top: 13px;
    display: block;
}

```

## File: source\Conference\Conference.Web\Content\time-n-place\time-n-place.css
```
/*
==============================================================================================================
Microsoft patterns & practices
CQRS Journey project
==============================================================================================================
2012 Microsoft. All rights reserved. Certain content used with permission from contributors
http://go.microsoft.com/fwlink/p/?LinkID=258575
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is 
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and limitations under the License.
==============================================================================================================
*/

.time-n-place {
    width: 240px;
    overflow: hidden;
    font-family: "Segoe UI light", Arial, sans-serif;
    margin-left: -6px;
}
.time-n-place__date {
    font-size: 70px;
    line-height: 1;
}
.time-n-place__time {
    font-size: 50px;
    line-height: 49px;
    margin-left: 1px;
}
.time-n-place__place {
    font-size: 32px;
    line-height: 66px;
    margin-left: 2px;
}
```

## File: source\Conference\Conference.Web\Scripts\_references.js
```
﻿/// <reference path="jquery-1.6.2.js" />

// ==============================================================================================================
// Microsoft patterns & practices
// CQRS Journey project
// ==============================================================================================================
// ©2012 Microsoft. All rights reserved. Certain content used with permission from contributors
// http://go.microsoft.com/fwlink/p/?LinkID=258575
// Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
// with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
// Unless required by applicable law or agreed to in writing, software distributed under the License is 
// distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
// See the License for the specific language governing permissions and limitations under the License.
// ==============================================================================================================

/// <reference path="jquery-ui-1.8.11.js" />
/// <reference path="jquery.validate.js" />
/// <reference path="knockout-2.0.0.debug.js" />
/// <reference path="modernizr-2.0.6-development-only.js" />
```

## File: source\Conference\Conference.Web.Public\Content\style.css
```
/*
==============================================================================================================
Microsoft patterns & practices
CQRS Journey project
==============================================================================================================
2012 Microsoft. All rights reserved. Certain content used with permission from contributors
http://go.microsoft.com/fwlink/p/?LinkID=258575
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is 
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and limitations under the License.
==============================================================================================================
*/

@import "common/common.css";
@import "page/page.css";
@import "quick/quick.css";
@import "footer/footer.css";
@import "likes/likes.css";
@import "content-main/content-main.css";
@import "tile/tile.css";
@import "time-n-place/time-n-place.css";
@import "menu/menu.css";
@import "content/content.css";
@import "nav/nav.css";
@import "form/form.css";
@import "reg-time-info/reg-time-info.css";
```

## File: source\Conference\Conference.Web.Public\Content\style.ie7.css
```
/*
==============================================================================================================
Microsoft patterns & practices
CQRS Journey project
==============================================================================================================
2012 Microsoft. All rights reserved. Certain content used with permission from contributors
http://go.microsoft.com/fwlink/p/?LinkID=258575
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is 
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and limitations under the License.
==============================================================================================================
*/

@import "form/form.ie7.css";
```

## File: source\Conference\Conference.Web.Public\Content\common\common.css
```
/*
==============================================================================================================
Microsoft patterns & practices
CQRS Journey project
==============================================================================================================
©2012 Microsoft. All rights reserved. Certain content used with permission from contributors
http://go.microsoft.com/fwlink/p/?LinkID=258575
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is 
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and limitations under the License.
==============================================================================================================
*/

h1, h2, h3, h4, h5, h6, p, blockquote, pre, a, abbr, acronym, address, big, cite, code, del, dfn, em, img, ins, kbd, q, s, samp, small, strike, sub, sup, tt, var, b, u, i, center, dl, dt, dd, ol, ul, li, fieldset, form, label, legend, table, caption, tbody, tfoot, thead, tr, th, td {
    margin: 0;
    padding: 0;
    border: 0;
    outline: 0;
    font-weight: normal;
    text-align: left;
    vertical-align: baseline;
    background: transparent;
    font-size: 100%;
    line-height: 16px;}
ol, ul { list-style: none; }
table { border-collapse: collapse; border-spacing: 0;}
html {
    overflow-x: visible;
    overflow-y: scroll;
    height: 100%;
}
body {
    margin: 0;
    padding: 0;
    font-family: "Segoe UI", "Arial", sans-serif;
    font-size: 13px;
    line-height: 16px;
}
label, input[type="button"], input[type="submit"], button {
    cursor: pointer;
}
input, select, button, textarea {
    font-family: "Segoe UI", "Arial", sans-serif;
    margin: 0;
}
input[type="radio"] {
    margin: 0;
}
select {
    height: 22px;
}
blockquote, q {
    quotes: none;
}
blockquote:before, blockquote:after,
q:before, q:after {
    content: '';
    content: none;
}
/*ссылки*/
a{outline: none; color: #fff;text-decoration: underline;}
a:hover {color: #66ccff;}
/*очистка*/
.g-clear {overflow: hidden;clear: both;font-size: 0; height: 0;}

input {
    text-align: left;
}
input[type=tel],
input[type=text],
input[type=number] {
    border-radius: 0;
    -webkit-border-radius: 0;
}


/* Styles for validation helpers
-----------------------------------------------------------*/
.field-validation-error
{
    color: #ff0000;
}

.field-validation-valid
{
    display: none;
}

.input-validation-error
{
    border: 1px solid #ff0000;
    background-color: #ffaaaa;
}

.validation-summary-errors
{
    font-weight: bold;
    color: #FFFF00;
}

.validation-summary-valid
{
    display: none;
}
```

## File: source\Conference\Conference.Web.Public\Content\content\content.css
```
/*
==============================================================================================================
Microsoft patterns & practices
CQRS Journey project
==============================================================================================================
2012 Microsoft. All rights reserved. Certain content used with permission from contributors
http://go.microsoft.com/fwlink/p/?LinkID=258575
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is 
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and limitations under the License.
==============================================================================================================
*/

.content {
    background: #2f7d00;
    min-height: 30px;
    padding: 20px;
}
.content_error {
	background: #cc6600;
	}
.content_error__txt {
	font-size: 15px;
	}
.content p {
    padding-top: 5px;
    line-height: 18px;
}
.content h3 {
    font-size: 20px;
    line-height: 1;
    padding-top: 21px;
    padding-bottom: 20px;
}
.content table {
    width: 100%;
    vertical-align: top;
}
.content th {
    padding: 5px 25px 8px 10px;
    background: #205501;
    border-bottom: 1px solid #2f7d00;
    vertical-align: top;
    font-size: 13px;
}
.content td {
    padding: 13px 20px 18px 10px;
    border-bottom: 1px solid #2f7d00;
    
    background: #fff;
    color: #000;
    vertical-align: top;
    font-size: 15px;
}
.content__link_pseudo {
    color: #0066cc;
    border-bottom: 1px dashed;
    text-decoration: none;
    line-height: 15px;
    display: inline-block;
}
.content .content__table-cell_right {
    text-align: right;
    padding-right: 0;
}
.content .content__table-cell_left {

}
.content__table_first-cell-wide td:first-child {
    width: 255px;
}

.content .content__note {
    letter-spacing: -1px;
    color: #999999;
    line-height: 13px;
    font-size: 11px;
}
.content .content__cell_total {
    font-weight: bold;
    font-size: 20px;
}
.content select{
    width: 61px;
}
.content tr.content__table__error td {
    border-top: solid 2px #ff6600;
	border-bottom: solid 2px #ff6600;
}
.content tr.content__table__error td:first-child {
    background: #fff url(content__table__error.gif) left top repeat-y;
}
.content tr.content__table__error td:last-child {
    background: #fff url(content__table__error.gif) right top repeat-y;
}
.content td.content__table__error-info {
	background: #ff6600;
	width: auto;
	color: #fff;
	padding: 2px 20px 3px 10px;
	line-height: 33px;
	}
```

## File: source\Conference\Conference.Web.Public\Content\content-main\content-main.css
```
/*
==============================================================================================================
Microsoft patterns & practices
CQRS Journey project
==============================================================================================================
2012 Microsoft. All rights reserved. Certain content used with permission from contributors
http://go.microsoft.com/fwlink/p/?LinkID=258575
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is 
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and limitations under the License.
==============================================================================================================
*/

.content-main {
    min-height: 355px;
    position: relative;
}
.content-main__wrapper {
    float: left;
    width: 1130px;
    }
    .content-main__main {
        margin: 0 425px 0 250px;
    }
    *:first-child+html .content-main__main {
        zoom:1;
        padding-bottom: 10px;
    }

.content-main__aside {
    float: left;
    width: 250px;
    margin-left: -1130px;
    padding-bottom: 170px;
}
.content-main__extra {
    float: left;
    width: 425px;
    margin-left: -425px;
}



.content-main_register {width: 1020px;padding: 0;}
.content-main_register .content-main__wrapper {
    width: auto;
    float: none;
    }
    *:first-child+html .content-main_register .content-main__main {padding: 0; }
    .content-main_register .content-main__main {
        float: left;
        margin: 0;
        width: 700px;
        }
.content-main_register .content-main__aside {
    float: right;
    width: 300px;
    margin: 0;
    padding: 0;
}


.content-main__time-n-place {
    height: 175px;
    margin-top: -175px;
    position: absolute;
}

.content-main__header {
    font-size: 28px;
    line-height: 27px;
    height: 40px;
    padding-bottom: 5px;
    font-family: "Segoe UI light", Arial, sans-serif;
    overflow: hidden;
	padding-top: 34px;
}
.content-main__extra-right {
    float: right;
}
.content-main__extra-left {
    float: left;
    width: 260px;
}
.content-main__nav {
    padding: 21px 19px 10px;
}

.content-main_assignseats {width: 1020px;padding: 0;}
.content-main_main_assignseats .content-main__wrapper {
    width: auto;
    float: none;
    }
    *:first-child+html .content-main_main_assignseats .content-main__main {padding: 0; }
    .content-main_assignseats .content-main__main {
        float: left;
        margin: 0;
        width: 800px;
        }
.content-main_assignseats .content-main__aside {
    float: right;
    width: 300px;
    margin: 0;
    padding: 0;
}
```

## File: source\Conference\Conference.Web.Public\Content\footer\footer.css
```
/*
==============================================================================================================
Microsoft patterns & practices
CQRS Journey project
==============================================================================================================
2012 Microsoft. All rights reserved. Certain content used with permission from contributors
http://go.microsoft.com/fwlink/p/?LinkID=258575
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is 
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and limitations under the License.
==============================================================================================================
*/

.footer {
	min-height: 100px;
    width: 1130px;
	margin: 0 auto 0;
	}
footer {
	font-size: 11px;
	min-height: 100px;
    width: 1130px;
    margin: 55px auto 0;
}
.footer__logo {
    margin: 1px 0 0 -2px;
    float: left;
}
.footer__content {
    margin-left: 250px;
}
.footer__content p {padding-top: 12px;}
.footer__content p:first-child {padding-top: 0;}
.footer__content a {
    text-decoration: none;
    border-bottom: 1px solid;
}
.footer__disclaimer {
    text-transform: uppercase;
    color:bisque;
    font-weight: bold;
}
```

## File: source\Conference\Conference.Web.Public\Content\form\form.css
```
/*
==============================================================================================================
Microsoft patterns & practices
CQRS Journey project
==============================================================================================================
2012 Microsoft. All rights reserved. Certain content used with permission from contributors
http://go.microsoft.com/fwlink/p/?LinkID=258575
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is 
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and limitations under the License.
==============================================================================================================
*/

.form {
	
	}
.form__fieldset {
	margin: 0; padding: 0;
	width: 320px;
	}
.form__fieldset:nth-child(odd) {
	float: left;
	}
.form__fieldset:nth-child(even) {
	float: right;
	}
.form__label {
	font-size: 15px;
	padding: 15px 0 0;
	display: block;
	}
.form__field {
	border: solid 1px #abadb3;
	padding: 0 7px 0;
	background: #fff;
	margin: 3px 0 0;
	}
.form__field input {
	width: 100%;
	margin: 0 0 0 0;
	text-align: left;
	border: none; padding: 0;
	font-size: 15px;
	color: #333333;
	height: 24px; line-height: 24px;
	}
.form__rb_m {
	margin: 10px 0 15px 0;
	}
.form__rb {
	
	}
.form__rb__title {
	display: inline;
	font-size: 15px;
	padding: 0 20px 0 0;
	}
.form__rb__item {
	padding: 0 15px 0 25px;
	font-size: 15px;
}
.form__rb__item input {
    width: 16px;
    height: 16px;
	background: url(form__rb__item.png) left 2px no-repeat;
    padding: 3px 5px 3px 0;
}
.form__rb__item input:checked {
	background: url(form__rb__item_a.png) left 2px no-repeat;
}
.form__chb {
	margin: 15px 0 0;
	}
.form__chb__item {
	background: url(form__chb__item.png) left 0 no-repeat;
	padding: 0 0 0 35px;
	line-height: 20px;
	font-size: 15px;
	}
div.form__chb__item {
	background: url(form__chb__item.png) left 0 no-repeat;
	cursor: pointer;
	display: inline;
	}
.form__chb__item_a {
	background: url(form__chb__item_a.png) left 0 no-repeat;
	}
div.form__chb__item_a {
	background: url(form__chb__item_a.png) left 0 no-repeat;
	}
.form__chb_seats {
	padding: 0 0 0;
	height: 31px;
	line-height: 40px;
	}
.form__seats-select {
	display: inline;
	line-height: 20px;
	font-size: 15px;
	display: none;
	}
.form .form-select-pad {
	top: 0;
	margin: 3px 0 0;
	}
.form-select-pad {
	position: relative;
	top: -5px;
	}
.form__seats-select .form-select-pad {
	top: 0;
	display: inline-block;
	}
.form-select {
	border: solid 1px #abadb3;
	position: relative;
	height: 24px;
	min-width: 59px;
	background: #ffffff;
	}
.form__seats-select .form-select {
	display: inline-block;
	}
.form-select__drop-down {
	position: absolute;
	right: 1px;
	top: 1px;
	width: 22px; height: 22px;
	background: #205501 url(form-select__drop-down.png) 50% 9px no-repeat;
	cursor: pointer;
	}
.form__seats-select .form-select__drop-down {
	background: #b42f03 url(form-select__drop-down.png) 50% 9px no-repeat;
	}
.form-select__active {
	height: 24px;
	line-height: 24px;
	color: #1c2126;
	font-size: 15px;
	padding: 0 30px 0 5px;
	cursor: pointer;
	}
div.form-select__options {
	background: #fff;
	border: solid 1px #abadb3;
	position: absolute;
	left: -1px;
	top: 24px;
	width: 100%;
	max-height: 124px;
	overflow: auto;
    z-index: 50;
	}
.form-select__options__active-item,.form-select__options__item {
	height: 24px;
	line-height: 24px;
	color: #1c2126;
	font-size: 15px;
	padding: 0 5px 0 5px;
	}
.form-select__options__active-item:hover,.form-select__options__item:hover {
	background: #ddd;
	}
.form-select__options__active-item {
	display: none;
	}
	
.form-promo {
	display: none;
	height: 26px;
	margin: -3px 0 0;
	}
.form-promo__txt {
	width: 175px;
	height: 24px;
	border: solid 1px #abadb3;
	font-size: 15px;
	line-height: 24px;
	color: #1c2126;
	float: left;
	margin-right: 5px;
	padding: 0 7px;
	text-align: left;
	}
.form-promo__but {
	width: 66px;
	height: 26px;
	color: #fff;
	background: #205501;
	font-size: 15px;
	line-height: 26px;
	border: none;
	}

```

## File: source\Conference\Conference.Web.Public\Content\form\form.ie7.css
```
/*
==============================================================================================================
Microsoft patterns & practices
CQRS Journey project
==============================================================================================================
2012 Microsoft. All rights reserved. Certain content used with permission from contributors
http://go.microsoft.com/fwlink/p/?LinkID=258575
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is 
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and limitations under the License.
==============================================================================================================
*/

.form__chb__item .form-select-pad {
	display: inline;
	}
.form__chb__item .form-select {
	display: inline;
	}
```

## File: source\Conference\Conference.Web.Public\Content\form\form.js
```
// ==============================================================================================================
// Microsoft patterns & practices
// CQRS Journey project
// ==============================================================================================================
// 2012 Microsoft. All rights reserved. Certain content used with permission from contributors
// http://go.microsoft.com/fwlink/p/?LinkID=258575
// Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
// with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
// Unless required by applicable law or agreed to in writing, software distributed under the License is 
// distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
// See the License for the specific language governing permissions and limitations under the License.
// ==============================================================================================================

$.fn.jsSelect = function() {
	var JsSelect__template = '<div class="form-select-pad">' +
		'<div class="form-select js-select">' +
			'<span class="form-select__drop-down"><span></span></span>' +
			'<div class="form-select__active js-current"></div>' +
			'<div class="form-select__options js-options" style="display: none;"><ul class="form-select__options"></ul></div>' +
		'</div>' +	
		'<input class="js-input" type="hidden"/>' +
	'</div>';
	
	
	var $cont = null;
	var valueLabels = {};
	var isOptionsOpen = false;
	
	var init = function($select) {
		$cont = $(JsSelect__template);	
		initClassAndName($select);
		initOptions($select);
		setValue($select.val());
		$select.replaceWith($cont);
		//handlers
		$cont.find('.js-select').click(onClickSelect);
		$cont.find('.js-options li.form-select__options__item').click(onClickOption);
		$(document.body).click(onBodyClick);
	};
	
	var initClassAndName = function($select) {
		if($select[0].className) {
			$cont.addClass($select[0].className);
		}
		$cont.find('.js-input').attr('name', $select.attr('name'));
	};
	
	var initOptions = function($select) {
		var options = $select[0].options;
		$cont.find('.js-options ul').append('<li class="form-select__options__active-item js-current"></li>');
		for(var i=0; i<options.length; i++) {
			var option = options[i];
			valueLabels[option.value] = option.text;
			
			var $opt = $('<li class="form-select__options__item"/>');
			$opt.text(option.text);
			$opt.data('val', option.value);
			if(option.value == $select.val())
				$opt.show();
			$cont.find('.js-options ul').append($opt);
		}
	};
	
	var setValue = function(value) {
		var label = valueLabels[value];
		$cont.find('.js-current').text(label);
		$cont.find('.js-input').val(value).change();
	};
	
	var onClickSelect = function() {
		if(!isOptionsOpen) {
			$cont.find('.js-options').show();
			isOptionsOpen = true;
			return false;
		}
	};
	
	var onBodyClick = function() {
		if(isOptionsOpen) {
			$cont.find('.js-options').hide();
			isOptionsOpen = false;
		}
	};
	
	var onClickOption = function() {
		setValue($(this).data('val'));
		$('.form-select__options__item').show();
	};
	
	init(this);
};


$(function() {
	$('select').each(function(){
		$(this).jsSelect();
	});

    $(window).bind('form-reload', function(e, data) {
        data.$form.find('select').each(function(){
            $(this).jsSelect();
        });
    });
	
	$('.js-radiobutton input').change(function(){
		$('.js-radiobutton-box').hide();
		$('.nav__right-small').hide();
		$('.js-radiobutton input:checked').each(function () {
		    var name = $(this).parent().attr('name');
		    $('.' + name + '-box').show();
		    $('.' + name + '-proceed').show();
		});
	});
	
	$('.js-checkbox').click(function(){
		$(this).toggleClass('form__chb__item_a');
	});
	
	$('.js-checkbox-seats').click(function(){
		$(this).toggleClass('form__chb__item_a');
		$('.form__seats-select').toggle();
	});
	
	$('.j-promocode-field').click(function(){
		$(this).hide();
		$('.form-promo').show();
		return false;
	});
});
```

## File: source\Conference\Conference.Web.Public\Content\likes\likes.css
```
/*
==============================================================================================================
Microsoft patterns & practices
CQRS Journey project
==============================================================================================================
2012 Microsoft. All rights reserved. Certain content used with permission from contributors
http://go.microsoft.com/fwlink/p/?LinkID=258575
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is 
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and limitations under the License.
==============================================================================================================
*/

.likes {}
.likes__link {
    margin-left: 10px;
    display: inline-block;
    width: 21px;
    height: 21px;
    background: url(likes_sprite.png);
}
*:first-child+html .likes__link {
    display: inline;
    zoom:1;
}
.likes__link_facebook {
    background-position: 0 0;
}
.likes__link_mail {
    background-position: -21px 0;
}
.likes__link_twitter {
    background-position: -42px 0;
}
```

## File: source\Conference\Conference.Web.Public\Content\menu\menu.css
```
/*
==============================================================================================================
Microsoft patterns & practices
CQRS Journey project
==============================================================================================================
2012 Microsoft. All rights reserved. Certain content used with permission from contributors
http://go.microsoft.com/fwlink/p/?LinkID=258575
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is 
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and limitations under the License.
==============================================================================================================
*/

.menu {
}
.menu__list {
    overflow: hidden;
    padding-top: 8px;
    }
.menu__item {
    float: left;
    margin-right: 23px;
    }
    .menu__item_active {
        font-weight: bold;
        color: #fff;
        }
.menu__item a {
    color: #cccccc;
    text-decoration: none;
    }
.menu__item a:hover {
	color: #66ccff;
	}
.menu__back {
    width: 32px;
    display: inline-block;
    height: 32px;
    background: url(menu__back.png);
    margin-right: 5px;
    position: relative;
    top: -8px;
    }
```

## File: source\Conference\Conference.Web.Public\Content\nav\nav.css
```
/*
==============================================================================================================
Microsoft patterns & practices
CQRS Journey project
==============================================================================================================
2012 Microsoft. All rights reserved. Certain content used with permission from contributors
http://go.microsoft.com/fwlink/p/?LinkID=258575
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is 
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and limitations under the License.
==============================================================================================================
*/

.nav {
    overflow: hidden;
    font-family: "Segoe UI light";
    font-size: 36px;
	padding: 20px 0 0 0;
}
.nav__left,
.nav__right {
    min-height: 40px;
    text-decoration: none;
    line-height: 28px;
    padding-bottom: 9px;
	border: none;
	font-family: "Segoe UI light";
    font-size: 36px;
}
.nav__left {
    background:no-repeat left 1px url(nav__left.png);
    padding-left: 48px;
    float: left;
    color: #0099ff;
	text-align: right;
}
.nav__left:hover {
	background:no-repeat left 1px url(nav__left_a.png);
	color: #33ccff;
	}
.nav__right {
    background:no-repeat right 1px url(nav__right.png);
    padding-right: 48px;
    float: right;
    color: #ff9900;
	text-align: right;
	}
.nav__right:hover {
    background:no-repeat right 1px url(nav__right_a.png);
	color: #ffcc33;
	}
.nav__right-small {
    text-decoration: none;
	font-size: 13px;
	display: block;
	margin: 5px 0 0 0;
	}
```

## File: source\Conference\Conference.Web.Public\Content\page\page.css
```
/*
==============================================================================================================
Microsoft patterns & practices
CQRS Journey project
==============================================================================================================
2012 Microsoft. All rights reserved. Certain content used with permission from contributors
http://go.microsoft.com/fwlink/p/?LinkID=258575
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is 
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and limitations under the License.
==============================================================================================================
*/

.page {
    min-height: 100%;
    color: #fff;
    background: #183b56;
}
.page__wrapper {
    width: 1130px;
    margin: 0 auto;
}
.page_registration .page__wrapper {
    width: 1070px;
    padding-left: 60px;
}
nav {
    height: 22px;
    background: #0e2d44;
    padding-top: 4px;
}
.page__head {
    padding-top: 37px;
    padding-bottom: 13px;
    overflow: hidden;
    position: relative;
    left: -2px;
    min-height: 75px;
    font-size: 45px;
    font-family: "Segoe UI light", Arial, sans-serif;
    line-height: 32px;
    }
    .page__head-note {
        font-size: 28px;
        }
.page__content {}

.page__likes {
    margin-top: 20px;
    }
    .page__likes .page__wrapper {
        width: 943px;
        padding-right: 187px;
        text-align: right;
    }
.page__menu {
    margin: 23px auto -10px;
    width: 1130px;
}

```

## File: source\Conference\Conference.Web.Public\Content\quick\quick.css
```
/*
==============================================================================================================
Microsoft patterns & practices
CQRS Journey project
==============================================================================================================
2012 Microsoft. All rights reserved. Certain content used with permission from contributors
http://go.microsoft.com/fwlink/p/?LinkID=258575
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is 
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and limitations under the License.
==============================================================================================================
*/

.quick {
    color: #cccccc;
    font-size: 11px;
    overflow: hidden;
}
.quick__list {
    float: left;
}
.quick__item {
    float: left;
    margin-right: 18px;
}
.quick__item a {
    color: #cccccc;
    text-decoration: none;
}
.quick__item a:hover {
	color: #66ccff;
	}
.quick__login {
    float: right;
    color: #cccccc;
    text-decoration: none;
}
.quick__item_bold a {
    font-weight: bold;
}

```

## File: source\Conference\Conference.Web.Public\Content\reg-time-info\reg-time-info.css
```
/*
==============================================================================================================
Microsoft patterns & practices
CQRS Journey project
==============================================================================================================
2012 Microsoft. All rights reserved. Certain content used with permission from contributors
http://go.microsoft.com/fwlink/p/?LinkID=258575
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is 
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and limitations under the License.
==============================================================================================================
*/

.reg-time-info {
	background: #0087b5 url(reg-time-info.png) 20px 20px no-repeat;
	padding: 10px 30px 18px 20px;
	min-height: 88px;
	position: absolute;
	left: 50%;
	top: 0px;
	width: 210px;
	margin: 79px 0 0 265px;
	}
.reg-time-info_fixed {
	position: fixed;
	left: 50%;
	top: 0;
	}
.reg-time-info__title {
	font-size: 45px;
	line-height: 45px;
	padding: 10px 0 8px 65px;
	}
.reg-time-info__txt p {
	margin: 10px 0 0; padding: 0;
	}
```

## File: source\Conference\Conference.Web.Public\Content\reg-time-info\reg-time-info.js
```
// ==============================================================================================================
// Microsoft patterns & practices
// CQRS Journey project
// ==============================================================================================================
// 2012 Microsoft. All rights reserved. Certain content used with permission from contributors
// http://go.microsoft.com/fwlink/p/?LinkID=258575
// Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
// with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
// Unless required by applicable law or agreed to in writing, software distributed under the License is 
// distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
// See the License for the specific language governing permissions and limitations under the License.
// ==============================================================================================================

$(function() {
  var w = $(window);
  var rti = $('.reg-time-info');
    var currentScrollTop = 0;
	w.scroll(function(){ 
		currentScrollTop = w.scrollTop() - 285;
		rti.css('top', currentScrollTop > 0 ? currentScrollTop : 0);
    });


	var Conference = {};

    Conference.StartTimer = function(element, timeoutCallback, formatCallback) {
        timeoutCallback = (typeof timeoutCallback === 'undefined') ? Conference._DefaultTimeoutCallback(element) : timeoutCallback;
        formatCallback = (typeof formatCallback === 'undefined') ? Conference._DefaultFormatCallback : formatCallback;

        var targetDate = new Date(parseInt(element.getAttribute('data-targetDate')));

        var timerCallback = function() {
            var formattedMilliseconds = '';
            var currentDate = new Date();

            var dateDiff = targetDate.getTime() - currentDate.getTime();
            if (dateDiff > 0) {
                formattedMilliseconds = formatCallback(dateDiff);
                element.innerHTML = formattedMilliseconds;
                window.setTimeout(function() { timerCallback(); }, 1000);
            } else {
                timeoutCallback();
            }
        };

        timerCallback();
    };

    Conference._DefaultFormatCallback = function(milliseconds) {
        var totalSeconds = Math.floor(milliseconds / 1000);
        var seconds = totalSeconds % 60;
        var totalMinutes = Math.floor(totalSeconds / 60);
        var minutes = totalMinutes % 60;
        var totalHours = Math.floor(totalMinutes / 60);
        var hours = totalHours % 24;
        var days = Math.floor(totalHours / 24);

        var secondsPart = [((seconds >= 10) ? '' : '0'), seconds.toString()].join('');
        var minutesPart = [((minutes >= 10) ? '' : '0'), minutes.toString()].join('');
        var hoursPart = [((hours >= 10) ? '' : '0'), hours.toString()].join('');
        var daysPart = [((days >= 10) ? '' : '0'), days.toString()].join('');

        var result = '';

        if (days > 0) {
            result = [daysPart, hoursPart, minutesPart, secondsPart].join(':');
        } else if (hours > 0) {
            result = [hoursPart, minutesPart, secondsPart].join(':');
        } else {
            result = [minutesPart, secondsPart].join(':');
        }

        return result;
    };

    Conference._DefaultTimeoutCallback = function(element) {
        return function() {
            element.innerHTML = '';
        };
    };

    $('.reg-time-info__title').each(function() {
        var redirectUrl = this.getAttribute('data-redirectUrl');
        Conference.StartTimer(this, function() { window.location = redirectUrl; });
    });
});
```

## File: source\Conference\Conference.Web.Public\Content\table\table.css
```
/*
==============================================================================================================
Microsoft patterns & practices
CQRS Journey project
==============================================================================================================
2012 Microsoft. All rights reserved. Certain content used with permission from contributors
http://go.microsoft.com/fwlink/p/?LinkID=258575
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is 
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and limitations under the License.
==============================================================================================================
*/


```

## File: source\Conference\Conference.Web.Public\Content\tile\tile.css
```
/*
==============================================================================================================
Microsoft patterns & practices
CQRS Journey project
==============================================================================================================
2012 Microsoft. All rights reserved. Certain content used with permission from contributors
http://go.microsoft.com/fwlink/p/?LinkID=258575
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is 
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and limitations under the License.
==============================================================================================================
*/

.tile-slide {
	height:140px;
}
.tile {
    width: 240px;
    height: 140px;
    background: #2f7d00;
    position: relative;
    cursor: pointer;
    float: left;
    margin: 0 10px 10px 0;
    text-decoration: none;
	overflow: hidden;
}
.tile:hover {
	margin: -5px 5px 5px -5px;
	padding: 5px 5px 5px 5px;
	color: #fff;
	}
.tile__imgs {
	position: relative;
	margin: -5px 0 0 -5px;
	}
.tile__img {
	position: absolute;
	left: 0;
	top: 0;
	/*margin: -5px 0 0 -5px;*/
	}
.tile:hover .tile__img img {
	/*margin: 0;*/
	}
.tile__imgs {
	display: block;
	}
.tile__header {
    position: absolute;
    bottom: 0;
    padding-bottom: 3px;
    left: 0;
    font-size: 18px;
    line-height: 1;
    height: 18px;
    display: block;
	background: url(tile__header.png) repeat;
	width: 100%;
	padding: 5px 0 8px 10px;
	z-index: 50;
}
.tile:hover .tile__header {
	padding: 10px 0 13px 15px;
	}
.tile__img-container {
    margin-top: 20px;
    min-height: 68px;
    text-align: center;
    line-height: 68px;
    vertical-align: middle;
    display: block;
}


.tile__img-container img {
    vertical-align: middle;
}

.tile_narrow {
    width: 140px;
}
.tile_small {
    width: 128px;
    height: 40px;
    margin: 0;
    padding: 0;
}
.tile_small:hover {
	margin: -5px -5px 0 0;
	padding: 5px 5px 5px 5px;
	}
.tile_small .tile__header {
    font-size: 13px;
    line-height: 14px;
    font-family: "Segoe UI", Arial, sans-serif;
    position: static;
    overflow: hidden;
    height: auto;
    padding: 5px 0 0 0;
	width: auto;
}
.tile_small:hover .tile__header {
	padding: 5px 0 0 0;
	}
.tile_small img {
    float: left;
    margin: 11px 21px 11px 11px;
}

.tile_twitter {
    background: #0099cc;
    padding-left: 11px;
    padding-top: 5px;
    padding-right: 20px;
    width: 209px;
    height: 135px;
}
.tile_twitter:hover {
	margin: -5px 5px 5px -5px;
	padding: 10px 25px 5px 16px;
	}
.tile_twitter .tile__header {
    position: static;
    overflow: hidden;
    background:no-repeat left 5px url(tile_twitter.png);
    height: 30px;
    padding: 0 0 0 32px;
    font-size: 24px;
    line-height: 1;
    font-family: "Segoe UI light", Arial, sans-serif;
	width: auto;
}
.tile_twitter:hover .tile__header {
	padding: 0 0 0 32px;
	}
.tile__tweet,
.tile__twit {
    font-size: 13px;
    position: absolute;
    bottom: 9px;
    overflow: hidden;
    right: 20px;
    left: 11px;
    top: 50px;
    line-height: 16px;
    }
.tile_twitter:hover .tile__tweet {
	top: 55px;
	bottom: 14px;
	left: 16px;
	right: 25px;
	}
    .tile__nick {
        overflow: hidden;
        padding-right: 65px;
        font-size: 13px;
        font-weight: bold;
        line-height: 1;
        padding-bottom: 3px;
        display: block;
        }
        .tile__time {
            float: right;
            width: 65px;
            overflow: hidden;
            font-size: 11px;
            line-height: 1;
            height: 13px;
            text-align: right;
            margin-right: -65px;
        }
.tile_twitter .tile-slide{
	width: 209px;
	height:105px;
	position: relative;
	display: block;
	}
.tile-slide .tile__tweet {
	width: 209px;
	height: 81px;
	
	font-size: 13px;
    position: absolute;
    bottom: auto;
    overflow: hidden;
    right: 20px;
    left: 11px;
    top: 50px;
    line-height: 16px;
	padding: 10px 0 0;
	}

.tile_event {}
.tile__topic {
    font-weight: bold;
    line-height: 18px;
    padding-left: 10px;
    padding-top: 16px;
    display: block;
}
.tile__span {
    font-size: 11px;
    line-height: 1;
    padding-left: 10px;
    padding-top: 10px;
    display: block;
}
.tile__nav {
    display: inline-block;
    margin-left: 14px;
}
.tile__nav-item {
    margin-right: 5px;
    display: inline-block;
    text-decoration: none;
    border: 1px solid transparent;
    font: 0/0 Arial;
}
.tile__nav-item_active,
.tile__nav-item:hover {
    border-color: #fff;
}
.tile__nav-item i {
    font: 0/0 Arial;
    display: inline-block;
    width: 5px;
    height: 5px;
    background: #fff;
    margin: 1px;
}


.tile_register {
    background: #ff6600;
}
.tile_register .tile__header {
    margin: 0;
    padding: 16px 46px 5px 7px;
    position: static;
    font-size: 36px;
    line-height: 1;
    height: 36px;
    font-family: "Segoe UI light", Arial, sans-serif;
    display: inline-block;
    background: 100% 21px url(tile_register.png) no-repeat;
	width: auto;
}
.tile_register:hover .tile__header {
	padding: 16px 46px 5px 7px;
	}
.tile__note {
    line-height: 20px;
    padding-left: 10px;
    padding-top: 13px;
    display: block;
}

```

## File: source\Conference\Conference.Web.Public\Content\time-n-place\time-n-place.css
```
/*
==============================================================================================================
Microsoft patterns & practices
CQRS Journey project
==============================================================================================================
2012 Microsoft. All rights reserved. Certain content used with permission from contributors
http://go.microsoft.com/fwlink/p/?LinkID=258575
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is 
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and limitations under the License.
==============================================================================================================
*/

.time-n-place {
    width: 240px;
    overflow: hidden;
    font-family: "Segoe UI light", Arial, sans-serif;
    margin-left: -6px;
}
.time-n-place__date {
    font-size: 70px;
    line-height: 1;
}
.time-n-place__time {
    font-size: 50px;
    line-height: 49px;
    margin-left: 1px;
}
.time-n-place__place {
    font-size: 32px;
    line-height: 66px;
    margin-left: 2px;
}
```

## File: source\Conference\Conference.Web.Public\Scripts\main.js
```
// ==============================================================================================================
// Microsoft patterns & practices
// CQRS Journey project
// ==============================================================================================================
// 2012 Microsoft. All rights reserved. Certain content used with permission from contributors
// http://go.microsoft.com/fwlink/p/?LinkID=258575
// Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance 
// with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
// Unless required by applicable law or agreed to in writing, software distributed under the License is 
// distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
// See the License for the specific language governing permissions and limitations under the License.
// ==============================================================================================================

$(document).ready(function(){
	$.fn.cycle.defaults.speed   = 900;
	$.fn.cycle.defaults.timeout = 6000;
	
	var RSec = 0;
	var RTile = 0;
	
	$('.tile-slide').each(function(index) {
		$(this).cycle({
			fx:      'scrollDown', 
			speed:    400, 
			timeout:  0
        });
    });
	
	AnimateTile();
	
	function AnimateTile() {
		RSec = Math.floor(Math.random() *5000) + 1000;
		RTile = Math.floor(Math.random() *5);
		setTimeout(function() {						  
			  $('.tile-slide').eq(RTile).cycle('next');
			  AnimateTile();
			}, RSec);
	}
	
	/*
	var RSec = 0;
	$('.tile-slide').each(function(index) {
		RSec = Math.floor(Math.random() *20000) + 3000
		$(this).cycle({
			fx:      'scrollDown', 
			speed:    400, 
			timeout:  RSec
		});
	});
	*/
	
	
	/*var SliderPos = 0;
	var SliderLen = 0;
	var AnimateSpeed = 500;
	var AnimateDelay = AnimateSpeed + 800;
	$('.tile__imgs').each(function(index) {
		$(this).find('img').css({'display': 'none','z-index': 1,'opacity': 0});
		SliderLen = $(this).find('img').length;
		$(this).find('img:first').css({'display': 'block','z-index': SliderLen+1,'opacity': 1});
	});
	
	var hTimer = null;

	$(".tile").mouseenter(function(){
	  var self = this;
	  SliderPos = 0;
	  SliderLen = $(self).find('.tile__imgs>*').length;
	  
	  if(hTimer != null) clearInterval(hTimer);
	  
	  hTimer = setInterval(function() {						  
		  if(SliderLen!=SliderPos+1){
			$(self).find('.tile__imgs>*').eq(SliderPos).css({'display': 'block','z-index': SliderLen});
			$(self).find('.tile__imgs>*').eq(SliderPos+1).css({'display': 'block','z-index': SliderLen+1});
			$(self).find('.tile__imgs>*').eq(SliderPos).animate({'opacity': 0},AnimateSpeed);
			$(self).find('.tile__imgs>*').eq(SliderPos+1).animate({'opacity': 1},AnimateSpeed);
			$(self).find('.tile__imgs>*').eq(SliderPos).css({'display': 'block','z-index': 1});
			SliderPos++;
			} else {
				$(self).find('.tile__imgs>*').eq(SliderPos).css({'display': 'block','z-index': SliderLen});
				$(self).find('.tile__imgs>*').eq(0).css({'display': 'block','z-index': SliderLen+1});
				$(self).find('.tile__imgs>*').eq(SliderPos).animate({'opacity': 0},AnimateSpeed);
				$(self).find('.tile__imgs>*').eq(0).animate({'opacity': 1},AnimateSpeed);
				$(self).find('.tile__imgs>*').eq(SliderPos).css({'display': 'block','z-index': 1});
				SliderPos = 0;
			}
		}, AnimateDelay);				  
	}).mouseleave(function(){
	   if(hTimer != null) {
		 clearInterval(hTimer);
		 hTimer = null;
	   }
	   var self = this;
	   $(self).find('.tile__imgs>*').stop();
	   $(self).find('.tile__imgs>*').css({'display': 'none','z-index': 1,'opacity': 0});
	   $(self).find('.tile__imgs>*:first').css({'display': 'block','z-index': SliderLen+1,'opacity': 1});

	});*/

});

$(function () {
    function getTweets() {
        var $tweets = $("#tweets");
        if ($tweets.length > 0) {
            var search = $tweets.attr("data-search");
            var url = 'http://search.twitter.com/search.json?callback=?&q=' + search;
            $.getJSON(url, function(json) {
                var output = [];
                if (json.results) {
                    for (var i = 0, len = Math.min(json.results.length, 10); i < len; i++) {

                        var timeDifference = (new Date().getTime() - Date.parse(json.results[i].created_at)) / (60 * 1000);
                        var time;
                        if (timeDifference < 60) {
                            time = Math.round(timeDifference) + "m ago";
                        } else {
                            timeDifference = timeDifference / 60;
                            if (timeDifference < 24) {
                                time = Math.round(timeDifference) + "h ago";
                            } else {
                                time = Math.round(timeDifference / 24) + "d ago";
                            }
                        }
                        output.push('<span class="tile__tweet" style="left: 0px; top: 0px; display: inline; position: absolute;"><span class="tile__nick"><span class="tile__time">' + time + '</span>@' + json.results[i].from_user + '</span>' + json.results[i].text + '</span>');
                    }

                    //now select the #results element only once and append all the output at once, then slide it into view
                    $("#tweets").html(output.join(''));
                    $('.tile_twitter .tile-slide').cycle({
                        fx: 'scrollUp',
                        speed: 400,
                        timeout: 0
                    });
                } else {
                    setTimeout(getTweets, 2000);
                }
            });
        }
    }

    //run the getTweets function on document.ready
    getTweets();
});
```

## File: source\Migrations\Migrations-Readme.txt
```
IMPORTANT NOTE
--------------

The projects in this folder are not referenced by the final solution, and they do not build with the current 
state of the codebase. This is intentional.
They correspond to specific milestones in the journey and only make sense within the context of migrations from 
version to version. To reproduce the migration experience, please check out specific versions of the entire 
system tagged V2-pseudo-prod or V3-pseudo-prod in the git repository history.

See the Migration notes (http://go.microsoft.com/fwlink/?LinkID=259596) and chapters 6 and 7 of the Guide:
http://go.microsoft.com/fwlink/p/?LinkID=258556
http://go.microsoft.com/fwlink/p/?LinkID=258557
```

