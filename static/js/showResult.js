$(function () {
    $('input:radio[name="x_label"]').change(
    function(){
        if ($(this).is(':checked') && $(this).val() == 'number') {
            // append goes here
            $('#graphs_numbers').show();
            $('#graphs_date').hide();
        } else {
            //
            $('#graphs_date').show();
            $('#graphs_numbers').hide();
        }
    });

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

                while (stuSel.options.length > 1) {
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
                $('#graphs_numbers').empty();
                var graphs_0_num = $('#graphs_numbers').get(0);
                var graphs_num = $('#graphs_numbers');
                var graph_info_num = data.graph_info_num;
                for (var i = 0; i < graph_info_num.length; i ++) {
                    var gra_s = document.createElement('SPAN');
                    var gra = document.createElement('EMBED');
                    gra.setAttribute("type", "image/svg+xml");
                    gra.setAttribute("src", graph_info_num[i]);
                    gra.setAttribute("style", "max-width:500px");
                    gra_s.appendChild(gra);
                    graphs_num.append(gra_s);
                }

                $('#graphs_date').empty();
                var graphs_0_date = $('#graphs_date').get(0);
                var graphs_date = $('#graphs_date');
                var graph_info_date = data.graph_info_date;
                for (var i = 0; i < graph_info_date.length; i ++) {
                    var gra_s = document.createElement('SPAN');
                    var gra = document.createElement('EMBED');
                    gra.setAttribute("type", "image/svg+xml");
                    gra.setAttribute("src", graph_info_date[i]);
                    gra.setAttribute("style", "max-width:500px");
                    gra_s.appendChild(gra);
                    graphs_date.append(gra_s);
                }

                console.log(graphs_num);
                console.log(graphs_0_num);
                console.log(graph_info_num);
                console.log(graphs_date);
                console.log(graphs_0_date);
                console.log(graph_info_date);
                console.log(data);
            },
            error: function (error) {
                console.log(error);
            }

        });
    });
});