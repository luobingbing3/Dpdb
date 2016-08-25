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
                var stuSel = $('#student_select').get(0);

                while (stuSel.options.length > 0) {
                    stuSel.remove(stuSel.options.length - 1);
                }
                for (var i = 0; i < student_list.length; i++) {
                    var opt = document.createElement('option');
                    opt.text = student_list[i][0].toString().concat(" - ", student_list[i][1].toString());
                    opt.id = student_list[i][0];
                    stuSel.add(opt, null);
                }
                //document.getElementById("student_select").selectedIndex = 0;
                console.log(student_list);
                console.log(data);
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
    $('#student_select').change(function() {
        $.ajax({
            url: '/drawLines',
            data: {
                stu_id: $('#student_select option:selected').attr("id"),
                stu_text: $('#student_select option:selected').val()
            },
            dataType: 'JSON',
            type: 'GET',
            success: function (data){
                $('#graphs').empty();
                var graphs_0 = $('#graphs').get(0);
                var graphs = $('#graphs');
                var graph_info = data.graph_info;
                for (var i = 0; i < graph_info.length; i ++) {
                    var gra_s = document.createElement('SPAN');
                    var gra = document.createElement('EMBED');
                    gra.setAttribute("type", "image/svg+xml");
                    gra.setAttribute("src", graph_info[i]);
                    gra.setAttribute("style", "max-width:350px");
                    gra_s.appendChild(gra);
                    graphs.append(gra_s);
                }
                console.log(graphs);
                console.log(graphs_0);
                console.log(graph_info);
                console.log(data);
            },
            error: function (error) {
                console.log(error);
            }

        });
    });
});