$(document).ready(function () {
    $('[data-id]').click(function () {
        var reaction = $(this).data('id')
        var image_id = $('[data-imageid]').attr('data-imageid')
        var source = $('[data-type=image]').attr('src')

        $.ajax({
            url: '../timeline/vote',
            type: 'GET',
            data: {
                'reaction': reaction,
                'image_id': image_id
            }, success: function (data) {
                if (data.url == 'None') {
                    $('[data-change=myDiv]').html(`<h2>nothing to show</h2>`)
                } else {
                    $('[data-imageid]').attr('data-imageid', data.image_id)
                    $('[data-type=image]').attr('src', data.url)
                }
            }, error: function () {
                console.log('error')
            }
        })
    })
})