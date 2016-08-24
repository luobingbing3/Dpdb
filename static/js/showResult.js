$(function () {
    $('#coach_select').change(function () {
        $.ajax({
            url: '/filterStudent',
            data: {
                choice: $('#coach_select option:selected').attr("id")
            },
            dataType: 'JSON',
            type: 'GET',
            success: function (data) {
                var student_list = data.student_list;
                console.log(student_list);
                var stuSel = $('#student_select').get(0);

                while (stuSel.options.length > 1) {
                    stuSel.remove(stuSel.options.length - 1);
                }
                for (var i = 0; i < student_list.length; i++) {
                    var opt = document.createElement('option');
                    opt.text = student_list[i][0].toString().concat(" - ", student_list[i][1].toString());
                    opt.id = student_list[i][0];
                    stuSel.add(opt, null);
                }
                console.log(data);
            },
            error: function (error) {
                console.log(error);
                console.log("???")
            }

        });
    });
});