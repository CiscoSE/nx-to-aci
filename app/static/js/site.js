function set_up() {
    $('#apic_url').rules('add','required')
    $('#apic_username').rules('add','required')
    $('#apic_password').rules('add','required')
    $('#configuration').rules('add','required')
    if($('#tool_form').valid()){
        Sijax.request('set_up', [Sijax.getFormValues('#tool_form')]);
        $('#set_up_response').html('<img src="/static/images/loading.gif" style="height:20px" />');
    }
    $('#configuration').rules('remove','required')
    $('#apic_url').rules('remove','required')
    $('#apic_username').rules('remove','required')
    $('#apic_password').rules('remove','required')
}

/**
 * Creates a notification
 */
function create_notification(title, message, type, delay) {
    $.notify({
        // options
        title: '<strong>' + title + '</strong>',
        message: '<p>' + message + '</p>'
    },{
        // settings
        type: type,
        placement: {
            from: "top",
            align: "right"
        },
        animate: {
            enter: 'animated fadeInRight',
            exit: 'animated fadeOutRight'
        },
        delay: delay,
        template: '<div data-notify="container" class="col-xs-11 col-sm-2 alert alert-{0}" role="alert">' +
            '<button type="button" aria-hidden="true" class="close" data-notify="dismiss">×</button>' +
            '<span data-notify="icon"></span> ' +
            '<span data-notify="title">{1}</span> ' +
            '<span data-notify="message">{2}</span>' +
            '<div class="progress" data-notify="progressbar">' +
                '<div class="progress-bar progress-bar-{0}" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%;"></div>' +
            '</div>' +
            '<a href="{3}" target="{4}" data-notify="url"></a>' +
	    '</div>'
    });
}