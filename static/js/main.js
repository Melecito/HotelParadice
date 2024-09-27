(function ($) {
    "use strict";
    
    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        // $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        // return false;
    });


    // Date and time picker
    $('.date').datetimepicker({
        format: 'L'
    });
    $('.time').datetimepicker({
        format: 'LT'
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        margin: 30,
        dots: true,
        loop: true,
        center: true,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:3
            }
        }
    });
    
})(jQuery);



// document.getElementById('send-btn').addEventListener('click',sendMessage);
// document.getElementById('user-input').addEventListener('keypress',function(e){
//     if(e.key ==='Enter'){
//         sendMessage();
//     }
// });
// function sendMessage(){
//     const inputField = document.getElementById('user-input');
//     const userInput = inputField.value;
//     if(userInput.trim() !== ''){
//         displayMessage(userInput,'user');
//         inputField.value = '';
//         getBotResponse(userInput);
//     }
// }
// function displayMessage(message,sender){
//     const chatBox = document.getElementById('chat-box');
//     const messageElement = document.createElement('div');
//     messageElement.classList.add('message',sender);
//     messageElement.textContent = message;
//     chatBox.appendChild(messageElement);
//     chatBox.scrollTop = chatBox.scrollHeight;
// }



// function getBotResponse(userInput){
//     let botResponse = '';
//     if(userInput.toLowerCase().includes('hola')){
//         botResponse = '!Hola! ¿En que te puedo ayudar?';
//     }
//     else if(userInput.toLowerCase().includes('ayuda')){
//         botResponse = 'Necesitas ayuda en programacion? elige el lenguaje: ';
//     }
//     else if(userInput.toLowerCase().includes('javascript')){
//         botResponse = 'Javascript es un lenguaje para desarrollo web enfocado en el FrontEnd: ';
//     }
//     else if(userInput.toLowerCase().includes('c++')){
//         botResponse = 'C++ es un lenguaje orientado a objetos, excelente para aprender a programar: ';
//     }
//     else if(userInput.toLowerCase().includes('adios')){
//         botResponse = 'Adios que tengas un lindo dia: ';
//     }
//     else{
//         botResponse = 'Lo siento no entiendo tu pregunta.';
//     }
//     setTimeout(()=>{
//         displayMessage(botResponse,'bot');
//     }, 1000);

// }

// document.getElementById('send-button').addEventListener('click', sendMessage);

// function sendMessage() {
//     const userInput = document.getElementById('user-input').value;
    
//     if (userInput.trim() === '') return;

//     addMessageToChat('Usuario: ' + userInput);
    
//     fetch('/chat', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({ message: userInput })
//     })
//     .then(response => response.json())
//     .then(data => {
//         addMessageToChat('Bot: ' + data.reply);
//         document.getElementById('user-input').value = '';
//     });
// }

// function addMessageToChat(message) {
//     const chatBox = document.getElementById('chat-box');
//     const messageDiv = document.createElement('div');
//     messageDiv.textContent = message;
//     chatBox.appendChild(messageDiv);
// }

document.getElementById("send-btn").addEventListener("click", function() {
    const userInput = document.getElementById("user-input").value;
    
    if (userInput.trim()) {
        appendMessage("Usuario: " + userInput);
        document.getElementById("user-input").value = '';
        
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userInput })
        })
        .then(response => response.json())
        .then(data => appendMessage("Bot: " + data.response));
    }
});

function appendMessage(message) {
    const chatBox = document.getElementById("chat-box");
    const messageDiv = document.createElement("div");
    messageDiv.textContent = message;
    chatBox.appendChild(messageDiv);
    
    chatBox.scrollTop = chatBox.scrollHeight; // Desplazar hacia abajo
}
