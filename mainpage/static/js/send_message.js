$(document).on('submit', '#msg_submit', function(e){
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: 'mailbox',
        data:{
            name: $('#name').val();
            email: $('#email').val();
            message: $('#message');
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val();
        },
        success:function()
        {
            alert("Your message has been sent.");
        }
    });
})