window.onload = function() {
	document.getElementById("button").onclick=function() {click()};
	var token = "detteErEnMockUpToken";
	var expDate = (new Date()).getTime() + 10*60000;
	sessionStorage.setItem(token, expDate);
	}

function click() {
	console.log("click");
	var redirectUri = getInfo().redirect;
	var token = "detteErEnMockUpToken";
	var expDate = (new Date()).getTime() + 10*60000;
	sessionStorage.setItem(token, expDate);
	var name = document.getElementById("name").value;
	var pass = document.getElementById("password").value;
	if(name==="admin" && pass === "admin") {
		window.location = "http://" + redirectUri + "?token=" + token;
		console.log(sessionStorage.tokens);
	} else {
		alert("Wrong name or password - use 'admin' 'admin'.");
	}
}

function getInfo() {
	console.log("getinfo");
	var vars = {};
    var parts = window.location.href.replace(/[?#&]+([^=&]+)=([^&]*)/gi,    
    function(m,key,value) {
    	vars[key] = value;
    });
	return vars;
	}
