var date = new Date()
var new_date = date.toLocaleDateString('pt-BR')
let display_date= "Data:" + new_date

$(document).ready(function () {
    $("#display_date").html(display_date)
    $('#save_button').prop('disabled', true);
})

let predicted_emotion;
$(function () {
    $("#predict_button").click(function () {
        let input_data = {
            "text": $("#text").val()
        }
        $.ajax({
            type: 'POST',
            url: "/predict-emotion",
            data: JSON.stringify(input_data),
            dataType: "json",
            contentType: 'application/json',
            success: function (result) {
                $("#prediction").html(result.data.predicted_emotion)
                $("#emo_img_url").attr('src', result.data.predicted_emotion_img_url);
                $('#prediction').css("display", "");
                $('#emo_img_url').css("display", "");
                predicted_emotion = result.data.predicted_emotion
                $('#save_button').prop('disabled', false);
            },
            error: function (result) {
                alert(result.responseJSON.message)
            }
        });
    });

    //Escreva o código aqui para a chamada AJAX
    $('#save_button').click(function(){
        var save_data = {
            'Date': new_date,
            'Entry': $('#text').val(),
            'Emotion': predicted_emotion
        }
        $.ajax({
            type: 'POST',
            url: '/save-entry',
            data: JSON.stringify(save_data),
            dataType: 'json',
            contentType: 'application/json',
            success: function(){
                alert('Salvo com sucesso')
                window.location.reload()
            },
            error: function(result){
                alert(result.responseJSON.message)
            }
        })
    })


})
