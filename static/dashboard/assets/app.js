$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})

$(document).ready(function() {
    $('#NoteModal').modal('show');
});

if (window.location.href.indexOf("domains") != -1) {
    document.getElementById('domains').classList.add('active');
} else if (window.location.href.indexOf("gitdorks") != -1) {
    document.getElementById('gitdorks').classList.add('active');
} else if (window.location.href.indexOf("scope") != -1) {
    document.getElementById('scope').classList.add('active');
} else if (window.location.href.indexOf("ggdorks") != -1) {
    document.getElementById('ggdorks').classList.add('active');
} else if (window.location.href.indexOf("acquisitions") != -1) {
    document.getElementById('acq').classList.add('active');
} else if (window.location.href.indexOf("methodology") != -1) {
    document.getElementById('mtd').classList.add('active');
} else if (window.location.href.indexOf("mynotes") != -1) {
    document.getElementById('notes').classList.add('active');
} else if (window.location.href.indexOf("profile") != -1) {
    document.getElementById('profile').classList.add('active');
} else {
    document.getElementById('dashboard').classList.add('active');
}


let sidebarToggle = document.querySelector(".sidebarToggle");
sidebarToggle.addEventListener("click", function(){
    document.querySelector("body").classList.toggle("active");
    document.getElementById("sidebarToggle").classList.toggle("active");
    document.querySelector('.togglebtn').classList.toggle('togglearrow');
})

// Subdomain Enum Traiger Text Area Subdomains.
let = document.getElementById("sub").addEventListener('click', function (e) {
    if (e.target.checked == true) {
        document.getElementById("subs__content").removeAttribute("hidden");
    } else {
        document.getElementById("subs__content").setAttribute("hidden", "hidden");
    }
});
