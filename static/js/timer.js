console.log('grubed')

var c= new Date()

const timezone = Intl.DateTimeFormat("en-GB").format(c);

console.log(timezone)
function timer() {
    var now = new Date().getTime("en-GB")
    var dest = new Date(2020, 2, 18).getTime("en-GB")
    var diff = dest - now
    if (diff > 0) {
        var d = Math.floor(diff / (1000 * 60 * 60 * 24))
        var drest = diff % (1000 * 60 * 60 * 24)
        var h = Math.floor(drest / (1000 * 60 * 60))
        var hrest = drest % (1000 * 60 * 60)
        var m = Math.floor(hrest / (1000 * 60))
        var mrest = hrest % (1000 * 60)
        var s = Math.floor(mrest / (1000))

        document.getElementById('day').innerText = d + 'd'
        document.getElementById('hour').innerText = h + 'h'
        document.getElementById('min').innerText = m + 'm'
        document.getElementById('sec').innerText = s + 's'

        setTimeout(timer, 1000)
    } else {
        console.log('timeout')
    }
}
timer()