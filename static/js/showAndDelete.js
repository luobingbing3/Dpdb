var currentid;
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
                $('#table_').empty();
                var table_ = document.getElementById('table_');
                var e = document.createElement('table');
                e.id = "info_table";
                table_.appendChild(e);

                var student_list = data.student_list;
                var stuSel = $('#student_select').get(0);

                while (stuSel.options.length > 1) {
                    stuSel.remove(stuSel.options.length - 1);
                }
                if($('#coach_select option:selected').attr("id")!='0'){
                    var opt = document.createElement('option');
                    opt.text = 'All';
                    opt.id = '0';
                    stuSel.add(opt, null);

                    for (var i = 0; i < student_list.length; i++) {
                        var opt = document.createElement('option');
                        opt.text = student_list[i][0].toString().concat(" - ", student_list[i][1].toString());
                        opt.id = student_list[i][0];
                        stuSel.add(opt, null);
                    }
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
        if($('#student_select option:selected').attr("id") == '-1')
            {
                $('#table_').empty();
                var table_ = document.getElementById('table_');
                var e = document.createElement('table');
                e.id = "info_table";
                table_.appendChild(e);
                return;
            }
        $.ajax({
            url: '/showItems',
            data: {
                stu_id: $('#student_select option:selected').attr("id"),
                coach_id: $('#coach_select option:selected').attr("id"),
                stu_text: $('#student_select option:selected').val()
            },
            dataType: 'JSON',
            type: 'GET',
            success: function (data){
                $(window).resize(function(){
                    $("#info_table").setGridWidth($(window).width()*0.98);
                    $("#info_table").setGridHeight($(window).height()-350);
                });

                var editid = [];
                var deleteid = [];
                jQuery("#info_table").jqGrid({
                    url:'/showItems',
                   dataType: "json",
                    colNames:['id_', '教练ID', '学员ID', '日期', '课程次数', '体重（kg）',
                             '血压（高压）mmgh（运动前）', '血压（低压）mmgh（运动前）',
                             '心率（次/min）', '体脂（胸、三头）mm', '体脂（腹、髂）mm',
                             '体脂（大腿）mm', '体脂含量%', '胸围（最高处）cm',
                             '腰围（肚脐处）cm', '臀围cm', '腰臀比', '大臂围cm', '大腿围cm',
                             '小腿围cm', '推（俯卧撑）次', '拉（trx或引体向上）次',
                             '蹲（静蹲）s', '核心（平板支撑）s', '平衡（左）s', '平衡（右）s'],
                    colModel:[
                        {name:'id_',index:'id_', width:30, hidedlg:true, hidden: true},
                        {name:'教练ID',index:'教练ID', width:45, editable:false},
                        {name:'学员ID',index:'学员ID', width:45,editable:false},
                        //{name:'日期',index:'日期', width:65, align:"right",editable:false,formatter:"date",formatoptions:{srcformat:'D, d M Y H:i:s A',newformat:'ISO8601Short'}},
                        {name:'日期',index:'日期', width:65, align:"right",editable:false, sorttype:"date",  datefmt:'Y-m-d'},
                        {name:'课程次数',index:'课程次数', width:55, align:"right",editable:false},
                        {name:'体重（kg）',index:'体重（kg）', width:60,align:"right",editable:true},
                        {name:'血压（高压）mmgh（运动前）',index:'血压（高压）mmgh（运动前）', width:160, align:"right", sortable:false,editable:true},
                        {name:'血压（低压）mmgh（运动前）',index:'血压（低压）mmgh（运动前）', width:160, align:"right", editable:true},
                        {name:'心率（次/min）',index:'心率（次/min）', width:80, align:"right", editable:true},
                        {name:'体脂（胸、三头）mm',index:'体脂（胸、三头）mm', width:110, align:"right", editable:true},
                        {name:'体脂（腹、髂）mm',index:'体脂（腹、髂）mm', width:100, align:"right", editable:true},
                        {name:'体脂（大腿）mm',index:'体脂（大腿）mm', width:95, align:"right", editable:true},
                        {name:'体脂含量%',index:'体脂含量%', width:80, align:"right", editable:true},
                        {name:'胸围（最高处）cm',index:'胸围（最高处）cm', width:100, align:"right", editable:true},
                        {name:'腰围（肚脐处）cm',index:'腰围（肚脐处）cm', width:100, align:"right", editable:true},
                        {name:'臀围cm',index:'臀围cm', width:60, align:"right", editable:true},
                        {name:'腰臀比',index:'腰臀比', width:60, align:"right", editable:true},
                        {name:'大臂围cm',index:'大臂围cm', width:65, align:"right", editable:true},
                        {name:'大腿围cm',index:'大腿围cm', width:65, align:"right", editable:true},
                        {name:'小腿围cm',index:'小腿围cm', width:65, align:"right", editable:true},
                        {name:'推（俯卧撑）次',index:'推（俯卧撑）次', width:90, align:"right", editable:true},
                        {name:'拉（trx或引体向上）次',index:'拉（trx或引体向上）次', width:110, align:"right", editable:true},
                        {name:'蹲（静蹲）s',index:'蹲（静蹲）s', width:80, align:"right", editable:true},
                        {name:'核心（平板支撑）s',index:'核心（平板支撑）s', width:90, align:"right", editable:true},
                        {name:'平衡（左）s',index:'平衡（左）s', width:70, align:"right", editable:true},
                        {name:'平衡（右）s',index:'平衡（右）s', width:70, align:"right", editable:true}
                    ],
                    rowNum: -1,
                    rownumbers: true,
                    //rowList:[10,20,30,40,50,60,70,80,90,100],
                    sortname: 'id_',
                    viewrecords: true,
                    sortorder: "desc",
                    width: $(window).width()*0.98,
                    height: $(window).height()-350,
                    shrinkToFit:false,
                    onSelectRow: function(id){

                        currentid = id;
                        console.log(currentid)
                        jQuery("#delete_, #edit_").attr("disabled",false)
                    },
                    //caption: "选择结果表格"

                });
                $("#info_table")[0].addJSONData(data.selected_items)

                jQuery("#edit_").unbind('click').click(function(){
                    jQuery("#save_").attr("disabled",false)

                    jQuery('#info_table').jqGrid('editRow',currentid,
                    {
                        keys: true,
                        url: 'clientArray'
                    });
                   var currID = jQuery("#info_table").jqGrid('getCell', currentid,'id_')
                    if(editid.indexOf(currID)<0)
                        {editid.push(currID);}
                });

                jQuery("#delete_").unbind('click').click(function(){
                    jQuery("#save_").attr("disabled",false)
                    var currID = jQuery("#info_table").jqGrid('getCell', currentid,'id_')
                    if(editid.indexOf(currID)>-1)
                        {editid.splice(editid.indexOf(currID),1);}
                    deleteid.push(currID)
                    jQuery("#info_table").jqGrid('delRowData', currentid)
                    jQuery("#delete_, #edit_").attr("disabled",true)


                });
                jQuery("#save_").unbind('click').click(function(){
                    if(confirm("您确定要保存您的修改至数据库吗?")==false)
                        return
                    jQuery("#save_").attr("disabled",false)
                    var rowids = jQuery("#info_table").jqGrid('getDataIDs')
                    var rowids_col = jQuery("#info_table").jqGrid('getCol', "id_")
                    var rowdata = new Array()
                    for(var i=0; i<editid.length;i++){
                        var index = rowids_col.indexOf(editid[i]);
                        if(index>-1){
                            a = jQuery("#info_table").jqGrid('getRowData', rowids[index])
                            rowdata.push($.param(a))
                        }
                    }

                    $.ajax({
                            url: '/updateData',
                            contentType: "application/json;charset=utf-8",
                            data: {
                                delete_id: deleteid.join(","),
                                update_data: rowdata.join(",")
                            },
                            dataType: 'JSON',
                            type: 'GET',
                            success:function(data){
                                alert(data)
                            }
                            })
                    jQuery("#save_").attr("disabled",true)

                    console.log(rowids)
                    console.log(rowids_col)
                    console.log(rowdata)
                    console.log(editid)
                    console.log(deleteid)

                    deleteid = [];
                    editid = [];
                });
                jQuery("#info_table").jqGrid('navGrid',"#prowed3",{edit:false,add:false,del:false});
                console.log(data)
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});


