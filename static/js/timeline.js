$(document).ready(function () {
    $('[data-id]').click(function () {

        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

        var reaction = $(this).data('id')
        var image_id = $('[data-imageid]').attr('data-imageid')
        var source = $('[data-type=image]').attr('src')
        var csrftoken = getCookie('csrftoken');

        // $.ajax({
        //     url: '../timeline/vote',
        //     type: 'POST',
        //     data: {
        //         'reaction': reaction,
        //         'image_id': image_id,
        //     }, headers: { "X-CSRFToken": csrftoken },
        //     success: function (data) {
        //         if (data.url == 'None') {
        //             $('[data-change=myDiv]').html(`<h2>nothing to show</h2>`)
        //         } else {
        //             $('[data-imageid]').attr('data-imageid', data.image_id)
        //             $('[data-type=image]').attr('src', data.url)
        //         }
        //     }, error: function () {
        //         console.log('error')
        //     }
        // })
    })
})