$(document).ready(function () {
    console.log('grub')
    $('[data-sel=select_opt]').change(function () {
        var rank_order_name = $(this).find(':selected').val()
        console.log(rank_order_name)
    })
})