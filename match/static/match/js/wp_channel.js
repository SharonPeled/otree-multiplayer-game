$(function () {
    $status_span = $('span.status');
    $timer_span = $('span.timer');

    $timer_span.html(seconds_to_passive);

    var idleTime = 0,
        active = true;

    function send_status(status) {
        if (status !== active) {
            var status_string = status === true ? 'active' : 'passive';
            $status_span.html(status_string);
            active = status;
            var msg = {
                'status': status,
            };
            if (wp_socket.readyState === WebSocket.OPEN) {
                wp_socket.send(JSON.stringify(msg));
            }
            ;

        }
    };

    function restoreActiveStatus() {
        idleTime = 0;
        $('.to_passive').css('width', '100%').attr('aria-valuenow', 100);
        var time_left = seconds_to_passive - idleTime;
        var time_show = time_left >= 0 ? time_left : 0;
        $timer_span.html(time_show);
        send_status(true);
    }

    //Increment the idle time counter every second.
    var idleInterval = setInterval(timerIncrement, 1000); // 1 second

    //Zero the idle timer on mouse movement.
    $(this).on('keypress', restoreActiveStatus)
    $(this).on('mousemove', restoreActiveStatus)
    // $(this).keypress(restoreActiveStatus(e));


    function timerIncrement() {
        idleTime = idleTime + 1;
        var time_left = seconds_to_passive - idleTime;
        $('.to_passive').css('width', time_left / seconds_to_passive * 100 + '%').attr('aria-valuenow', time_left);
        var time_show = time_left >= 0 ? time_left : 0;
        $timer_span.html(time_show);
        if (idleTime > seconds_to_passive) {
            send_status(false);
            window.location.reload();
        }
    }
});