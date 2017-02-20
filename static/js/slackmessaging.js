$(document).ready(function()
{
	    /*function to auto-generate a CRSF cookie */
// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

// Sending message to admin

})

function sendToSlack(){
    // var settings = {
    //     url: "https://hooks.slack.com/services/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",
    //     method: "POST",
    //     dataType: "application/x-www-form-urlencoded",
    //     data: {
    //         "payload": JSON.stringify({text: $("message").val()})
    //     }

    // }
    // $.ajax(settings).done(function(response){
    //     console.log(response);
    // })

    var myJSONStr = 'payload= {
        "username": "SELF TEST",
        "text": "Just checking the message services"
    }';

    var xmlhttp = new XMLHttpRequest(),
        webhook_url = "https://hooks.slack.com/services/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",
        JSONmsg = myJSONStr.stringify();
    xmlhttp.open('POST', webhook_url, false);
    xmlhttp,setRequestHeader(JSON, 'application/x-www-form-urlencoded');
    xmlhttp.send(JSONmsg);

}