const questionsForm = document.getElementById('questionsForm');
const userMeta = document.querySelector('meta[name="username"]');
var timer;

//  Animation
window.addEventListener('load', () => {
    const type_user = `Hi ${userMeta.content}...`;

    setTimeout(() => {
        $("#user-card").addClass('animate');
        let typed = new Typed("#user", {
            strings: [type_user],
            typeSpeed: 90,
            backSpeed: 90,
            showCursor: false
        })
        $('#user').addClass('typing');
    }, 2800);
})


// Showing questions cards
$('#start-btn').click((e) => {

    e.target.disabled = true
    scrollTo(0, document.body.scrollHeight)
    questionsForm.classList.remove('d-none')

    $('.timer').removeClass('d-none')
    let minutes = 9, seconds = 60
    timer = setInterval(() => {
        seconds--
        if (seconds < 0) {
            minutes--
            seconds = 59
        }
        displayTimer(seconds, minutes)
        if (minutes == 0 && seconds == 0) {
            clearInterval(timer)
            $('.spinner').removeClass('d-none')
            questionsForm.submit();
        }
    }, 100);
})
function displayTimer(ss, mm) {
    if (mm == 0 && ss <= 59) {
        $('.minutes').addClass('text-danger')
        $('.seconds').addClass('text-danger')
    }
    mm = mm <= 9 ? '0' + mm : mm
    ss = ss <= 9 ? '0' + ss : ss
    $('.minutes').text(mm + " : ")
    $('.seconds').text(ss)
}
