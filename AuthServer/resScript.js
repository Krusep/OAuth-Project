window.onload = function() {
	uri = window.location.href;
	console.log(sessionStorage);
	var token = getInfo().token;
	if(sessionStorage[token] != undefined) {
		if(sessionStorage[token] >= new Date()) {
			alert("yay");
		} else {
			alert("Expired access token");
		}
	} else {
		alert("Invalid access token");
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
