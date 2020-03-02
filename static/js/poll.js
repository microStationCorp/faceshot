$(document).ready(function () {
    console.log('grub')
    $('[data-sel=select_opt]').change(function () {
        var rank_order_name = $(this).find(':selected').val()
        var myHtml = '<div class="row justify-content-center">'

        if (rank_order_name != 'None') {
            $.ajax({
                url: '../poll/pollajax',
                type: 'GET',
                data: {
                    'rank_order_name': rank_order_name
                },
                success: function (data) {
                    sl = 1
                    for (var img of data) {
                        myHtml = myHtml + `
                        <div class="card m-2 col-md-4 col-lg-3 p-2 border-dark" style="width: 10rem;">
                        <img class="card-img-top" src="${img.url}" alt="Card image cap"
                        height="150px" style="border: 2px solid rgb(22, 97, 97);">
                        <div class="card-body">
                        <h5 class="card-text">${img.caption}</h5>
                        </div>
                        <div class="card-text text-muted">Uploader : ${img.uploader} </div>
                        <div class="card-text">Rank : ${sl} </div>
                        <div class="card-text">Value : ${img.count}</div>
                        </div>
                        `
                        sl++
                    }
                    myHtml=myHtml+'</div>'
                    $('#ranked_image_continer').html(myHtml)
                },
                error: function (error) {
                    console.log(error)
                }
            })
        }

    })
})