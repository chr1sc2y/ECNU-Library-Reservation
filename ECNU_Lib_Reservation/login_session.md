{"ret":1,"act":"login","msg":"ok","data":{"id":"10132510139","accno":"9760293","name":"陈正宇","phone":"18701901620","email":"","msn":"","ident":"4194561","dept":"软件学院","deptid":"10190","tutor":null,"tutorid":null,"cls":"软件本科生2013级","clsid":"10191","receive":true,"tsta":null,"rtsta":null,"pro":null,"score":200,"credit":[["研究室惩罚规则","200","300",""]],"role":"134217730"},"ext":null}
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=EDGE" />
    <meta name="renderer" content="webkit">
    <title>IC空间管理系统</title>
    
    <script type="text/javascript" src="../../fm/jquery/jquery-1.7.2.min.js"></script>
    <script type="text/javascript" src="../../fm/jquery-ui/jquery-ui-1.10.3.custom.min.js"></script>
    <script type="text/javascript" src="../../fm/jquery-ui/bootstrap/js/bootstrap.js"></script>

    <script type="text/javascript" src="../../fm/uni.lib.js?v=1.0.0.20160604"></script>
    <link rel="stylesheet" type="text/css" href="../../fm/uni.css" />

    <script type="text/javascript" src="../../pro/pro.lib.js?v=1.0.0.20160604"></script>
    <link rel="stylesheet" type="text/css" href="../../pro/pro.css" />

    <link href="../../md/validationEngine/validationEngine.jquery.css" rel="stylesheet" />
    <script src="../../md/validationEngine/validationEngine.js" type="text/javascript"></script>

    <link href="../../md/PageCtrl/PageCtrl.css" rel="stylesheet" />
    <script src="../../md/PageCtrl/PageCtrl.js" type="text/javascript"></script>

<link rel="stylesheet" type="text/css" href="../a/theme/a.css" />
    <!--[if lt IE 9]>
      <script src="../../fm/add/html5shiv.js"></script>
      <script src="../../fm/add/respond.js"></script>
    <![endif]-->
    <script>
        $(function () {
            //初始化语言
            
            //backtop
            $(".back_top").backtop();
            //记录hr加载的网页地址
            $("body").on("uni_hr_load_success", function () {
                $(".by_hr_load").html(uni.hr.para.url || "无")
            });
            //浏览器检查
            if (uni.getIEVer() > 0) {
                if(uni.getIEVer() < 8)
                    uni.msg.error("您当前的浏览器版本太低，请升级浏览器至谷歌、火狐、IE9+等更高级的浏览器。");
                if (uni.getIEVer() < 9)
                    $("#warning_old_browser").show();
                else
                    $("#warning_old_browser").hide();
            }
        })
        //自定义
        var cus = {
            showLogin: function () {
                pro.d.lg.login();
            }
        }
    </script>
    
    <script src="../../md/unifloorplan/unifloorplan.js" type="text/javascript"></script>
    <link href="../../md/unifloorplan/unifloorplan.css" rel='stylesheet' />
    <script src="../../md/unicalendar/unicalendar.js" type="text/javascript"></script>
    <link href="../../md/unicalendar/unicalendar.sch.css" rel='stylesheet' />
    <link href="../../md/Timepickeraddon/jquery-ui-timepicker-addon.css" rel="stylesheet" />
    <script src="../../md/Timepickeraddon/jquery-ui-timepicker-addon.js" type="text/javascript"></script>
    <script src="../../md/Timepickeraddon/jquery-ui-timepicker-zh-CN.js" type="text/javascript"></script>
    <link rel="stylesheet" href="theme/cus.css" />
    <link rel="stylesheet" type="text/css" href="../../fm/jquery-ui/bootstrap/jquery-ui-1.10.3.custom.css" />
    <link rel="stylesheet" href="../../fm/jquery-ui/bootstrap/css/bootstrap.css" />
    <style>
        /*.affix { top: 20px; overflow: visible; white-space: nowrap; }
        .affix-bottom { position: absolute; }
        .affix-top { overflow: visible; white-space: nowrap; }*/
        .drop-select { min-width: 120px; }
        /*二级菜单*/
        #info_tree .cls_sec { overflow: hidden; height: 26px; margin-left: -12px; }
        #info_tree .cls_sec a.nav_cls_name { color: #666; padding-left: 6px; }
        #info_tree .cls_sec .glyphicon { color: #ccc; }
    </style>
    <script>
        //公共对象
        var content;//内容区域
        $(function () {
            //判断登录 异步登录
            cus.showLogin = function (parameter) {
                pro.d.lg.login(function (rlt, dlg) {
                    if (typeof (rlt.data) == "object" && rlt.data.id) {
                        pro.acc = rlt.data;
                        $("body").removeClass("login_state_out").addClass("login_state_in");
                        $(".acc_info .acc_info_name").html(pro.acc.name);
                        $(".acc_info .acc_info_id").html(pro.acc.id);
                        $(".acc_info .acc_info_dept").html(pro.acc.dept);
                        if (typeof (parameter) == "function") parameter();
                        else if (typeof (parameter) == "object" && typeof (parameter.callback) == "function") parameter.callback(parameter);
                        else { uni.msgBox("登录成功") }
                    }
                    dlg.dialog("close");
                }, null, "临时登录窗口！为不打断操作，登录后将不刷新页面。建议操作完成后手动刷新");
            }
            // 初始化公共对象
            content = $("#detail_con");
            //载入主页
            $(".click_load").clickLoad();
            $("#home").trigger("click");
            //$(".cls_list").change(function () {
            //    treeFiler();
            //    reloadInfo();
            //});
            //添加选中标志
            $(".it_list li,.click_load").click(function () {
                $(".it_list li,.click_load").removeClass("activity");
                $(this).addClass("activity");
            });
            $(".it_list li").click(function () {
                reloadInfo();
            });
        })
        //unicalendar配置
        var uni_calendar_dft_opt = {
            cusPrepare: function (data, callback) {
                var obj = data.obj;
                if (obj.type != "kind" && obj.prop && (parseInt(obj.prop) & 65536) > 0) {//是否支持开放活动 prop=65536这个属性是临时使用 所以暂定义在外层
                    var ov = "0";
                    var url = "../a/openaty.aspx?dev=" + obj.devId + "&devkind=" + obj.kindId + "&back=true&date=" + data.dt.replace(/-/g, "") + "&time=" + data.start;
                    if (ov == "1") {//可选
                        uni.confirm("本设备支持预约开放活动", function () {
                            uni.hr.loadHtml(url, null, null, data);
                        }, function () {
                            callback(data);
                        }, "", {okText:"开放活动",backText:"普通预约"});
                    }
                    else if (ov == "2") {//不可选
                        uni.hr.loadHtml(url, null, null, data);
                    }
                    else {
                        callback(data);
                    }
                }
                else {
                    callback(data);
                }
            },
            dev_order: "",
            kind_order: ""
        }
        //条件过滤
        function treeFiler() {
            var ul = $(".it_cls_list");
            var list = $(".nav_cls_li", ul);
            var ih = $("li:first", list).height();
            var sec = $(".cls_sec", ul).height(ih + "px");
            //list.click(function () {
            //    $(".cls_sec.activity", ul).animate({ height: ih + "px" }, "fast");
            //    //var pthis = $(this);
            //    //if (!pthis.hasClass("activity")) {
            //    //    if (pthis.hasClass("cls_sec")) {
            //    //        var height = ih * (pthis.find(".it").length + 1);
            //    //        pthis.animate({ height: height + "px" }, "fast");
            //    //    }
            //    //}
            //});
            list.click(function () {
                var pthis = $(this);
                var self = (pthis.hasClass("activity") && pthis.hasClass("cls_sec"));
                sec.each(function () {
                    var sthis = $(this);
                    if (sthis.find(".activity").length == 0) {
                        sthis.removeClass("activity");
                        sthis.animate({ height: ih + "px" }, "fast", function () {
                            sthis.find(".glyphicon").removeClass("glyphicon-circle-arrow-up").addClass("glyphicon-circle-arrow-down");
                        });
                    }
                });
                if (self) return;
                if (pthis.hasClass("cls_sec")) {
                    if (!pthis.hasClass("activity")) {
                        pthis.addClass("activity");
                        var height = ih * (pthis.find(".it").length + 1);
                        pthis.animate({ height: height + "px" }, "fast", function () {
                            pthis.find(".glyphicon").removeClass("glyphicon-circle-arrow-down").addClass("glyphicon-circle-arrow-up");
                        });
                    }
                    else {
                        pthis.removeClass("activity");
                    }
                }
            });
            //ul.mouseleave(function () {
            //    sec.each(function () {
            //        var pthis = $(this);
            //    if (pthis.find(".activity").length==0) {
            //        pthis.animate({ height: ih + "px" }, "fast", function () {
            //            pthis.find(".glyphicon").removeClass("glyphicon-circle-arrow-up").addClass("glyphicon-circle-arrow-down");
            //        });
            //    }
            //    });

            //});
        }
        //主动载入信息方法
        function reloadInfo() {
            var url = $(".it_list li.activity").attr("url");
            if (url) {
                uni.backTop();
                uni.hr.loadHtml(url, {}, content);
            }
        }
    </script>

</head>
<body style="background-color:#f7f7f7;" class="login_state_in">
    <div style="height:30px;background:#31B0D5;color:white;text-align:center;display:none;" id="warning_old_browser">
        您当前的浏览器版本较低，为获得更好的显示效果，建议升级浏览器至谷歌、火狐、IE9+等更高级的浏览器。
    </div>
    <div id="pub_resource">
        
<!--时间选择器-->
<div id="dlg_basic_dt_selecter" class="hidden">
    <table>
        <tbody class="tmp_time">
            <tr class="md_date">
                <td><span class="uni_trans">日期</span></td>
                <td>
                    <span class="mt_date"></span>
                </td>
            </tr>
            <tr class="md_date">
                <td><span class="uni_trans">时间</span></td>
                <td>
                    <div>
                        <span>
                            <select name="start_time" class="mt_start_time" style="width: 80px;"></select>
                        </span>
                        <span>&nbsp;-&nbsp;</span>
                        <span>
                            <select name="end_time" class="mt_end_time" style="width: 80px;"></select>
                            <a class="sub_picker hidden" onclick="$(this).parents('tr:first').remove();">&nbsp;<span class="glyphicon glyphicon-minus-sign text-danger"></span></a>
                            <a class="add_picker hidden">&nbsp;<span class="glyphicon glyphicon-plus-sign text-primary"></span></a></span>
                    </div>
                </td>
            </tr>
        </tbody>
        <tbody class="tmp_date">
            <tr class="md_date">
                <td><span class="uni_trans">开始日期</span></td>
                <td><span class="mt_date"></span>
                    <input type="hidden" name="start_date" class="mt_start_date control-form" style="width: 120px;" />
                    <input type="hidden" class="open_start" name="open_start" />
                    <input type="hidden" class="open_end" name="open_end" />
                </td>
            </tr>
            <tr class="md_date">
                <td><span class="uni_trans">结束日期</span></td>
                <td>
                    <select name="end_date" class="mt_end_date" style="width: 140px;"></select></td>
            </tr>
        </tbody>
        <tbody class="tmp_cycledate">
            <tr class="md_date">
                <td><span class="uni_trans">时间</span></td>
                <td>
                    <input type="hidden" name="start" class="cycle_start" />
                    <input type="hidden" name="end" class="cycle_end" />
                                <div class="btn-group">
                <button type="button" class="btn btn-info set_cycle_date"><span class="uni_trans">设置时间</span></button>
                <button type="button" class="btn btn-default calc_detail_date" disabled><span class="uni_trans">查看详细时间</span></button>
            </div>
                </td>
            </tr>
            <tr class="md_date">
                <td><span class="uni_trans">描述</span></td>
                <td><span class="uni_trans cycle_desc">时间未设置</span></td>
            </tr>
        </tbody>
        <tbody class="tmp_datetime">
            <tr class="md_date">
                <td><span class="uni_trans">开始时间</span></td>
                <td><span class="mt_date" style="width: 140px; display: inline-block;"></span>
                    <span>
                        <select name="start_time" class="mt_start_time" style="width: 80px;"></select></span>
                </td>
            </tr>
            <tr class="md_date">
                <td><span class="uni_trans">结束时间</span></td>
                <td>
                    <span style="width: 140px; display: inline-block;">
                        <select name="end_date" class="mt_end_date" style="width: 140px;"></select></span>
                    <span>
                        <select name="end_time" class="mt_end_time" style="width: 80px;"></select>
                        <a class="sub_picker hidden" onclick="$(this).parents('tr:first').remove();">&nbsp;<span class="glyphicon glyphicon-minus-sign text-danger"></span></a>
                        <a class="add_picker hidden">&nbsp;<span class="glyphicon glyphicon-plus-sign text-primary"></span></a></span>
                </td>
            </tr>
        </tbody>
        <tbody class="tmp_fix">
            <tr class="md_date">
                <td><span class="uni_trans">预约时段</span></td>
                <td>
                    <span>
                        <input type="hidden" name="start" class="mt_start" />
                        <input type="hidden" name="end" class="mt_end" />
                        <select class="mt_fix_time" style="width: 120px;"></select></span>
                </td>
            </tr>
        </tbody>
    </table>
</div>
<div id="dlg_basic_mb_add" class="hidden">
    <div class="tmp_complex">
        <div class="form-group" style="margin-bottom: 0;">
            <input type="hidden" name="group_id" class="group_id" />
            <input type='hidden' class="mb_list" name='mb_list' />
            <div class="btn-group">
                <button type="button" class="btn btn-default group_name" disabled><span class="uni_trans">小组未创建</span></button>
                <button type="button" class="btn btn-info set_group_mb"><span class="uni_trans">设置小组</span></button>
            </div>
        </div>
    </div>
    <div class="tmp_simple">
        <div>
            <input type="hidden" class="min_user" name="min_user" />
            <input type="hidden" class="max_user" name="max_user" />
            <input type='hidden' class="mb_list" name='mb_list' />
            <div class="input-group" style="width: 180px;">
                <span class="input-group-addon" title="姓名/登录名搜索">+</span>
                <input class="mb_name_ipt form-control hint" type="text" url="searchAccount.aspx" placeholder="姓名/登录名搜索" onclick="this.value = ''" />
            </div>
        </div>
        <div class="dialog">
            <div style="width: 200px; color: grey;"><span class="uni_trans">组成员名单</span></div>
            
        </div>
    </div>
</div>
<div id="dlg_basic_cycle_dt" class="hidden">
    <table>
        <tbody class="tmp_cycle">
            <tr>
                <td class="title text-right">选择日期：</td>
                <td>
                    <input type="text" class="date_start sel_date must" data-msg="开始日期必填" name="cycle_date_start" readonly="readonly">
                    <span class="single_hide">-
                    <input type="text" class="date_end sel_date must" data-msg="结束日期必填" name="cycle_date_end" readonly="readonly">
                    <span style="float: right;">&nbsp;<a class="click cmp_detail">查看详细日期</a>&nbsp;|&nbsp;<a class="click cvt_single_day">转单日时间</a>&nbsp;</span></span>
                    <span style="float: right;" class="cycle_hide">&nbsp;<a class="click cvt_cycle_day">转周期时间</a>&nbsp;</span>
                </td>
            </tr>
            <tr>
                <td class="title text-right">选择时间：</td>
                <td>
                    <input type="text" name="cycle_time_start" class="time_start sel_time must" data-msg="开始时间必填" readonly="readonly">
                    -
                    <input type="text" name="cycle_time_end" class="time_end sel_time must" data-msg="结束时间必填" readonly="readonly"></td>
            </tr>
            <tr class="single_hide">
                <td class="title text-right">时间周期：</td>
                <td>
                    <div class="sel_time_panel">
                        每&nbsp;<select name="cycle_freq" class="cycle_freq" style="width: 40px">
                            <option value="1" selected>1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="4">4</option>
                            <option value="5">5</option>
                            <option value="6">6</option>
                        </select>&nbsp;<select name="cycle_type" class="cycle_type">
                            <option value="d" selected>天</option>
                            <option value="w">周</option>
                            <option value="m">月</option>
                        </select>
                        <span class="view_week" style="display: none;">
                            <label>
                                <input type="checkbox" class="cycle_week" name="cycle_week" value="1" />星期一&nbsp;</label>
                            <label>
                                <input type="checkbox" class="cycle_week" name="cycle_week" value="2" />星期二&nbsp;</label>
                            <label>
                                <input type="checkbox" class="cycle_week" name="cycle_week" value="3" />星期三&nbsp;</label>
                            <label>
                                <input type="checkbox" class="cycle_week" name="cycle_week" value="4" />星期四&nbsp;</label>
                            <label>
                                <input type="checkbox" class="cycle_week" name="cycle_week" value="5" />星期五&nbsp;</label>
                            <label>
                                <input type="checkbox" class="cycle_week" name="cycle_week" value="6" />星期六&nbsp;</label>
                            <label>
                                <input type="checkbox" class="cycle_week" name="cycle_week" value="0" />星期日&nbsp;</label>
                        </span>
                        <span class="view_month" style="display: none;">，<input type="text" name="cycle_day" class="cycle_day must" data-msg="请选择日期" style="width: 40px;" />日
                        </span>
                    </div>
                </td>
            </tr>
        </tbody>
    </table>
</div>
<script>
    //基础模块
    pro.d.basic = {
        //添加时间选择器 panel 容器 obj 预约状态对象 type 选择器类别 obj参数除resvTimeClick需求外：时间[start] [end]日期[startDate] [endDate] 整日跨天需要openStart openEnd
        addDateTimePicker: function (panel, obj, type) {
            function dateSel($sel, v,dft) {
                $sel.html();
                var day = uni.parseDate(v + " 00:00");
                var end = Math.ceil((obj.max || 1440) / 1440);
                var start = Math.floor((obj.min || 0) / 1440);
                for (var i = 0; i < end; i++) {
                    var dt = day.format("yyyy-MM-dd");
                    $sel.append('<option value="' + dt + '">' + dt + '</option>');
                    day.addDays(1);
                }
                $sel.val(dft||v);
            }
            function timeInt(v) {
                if (v.length > 5)
                    v = v.substr(v.length - 5);
                var tmp = v.split(":");
                if (tmp.length < 2) return 0;
                return parseInt(tmp[0], 10) * 100 + parseInt(tmp[1], 10);
            }
            if (!uni.isNoNull([panel, obj, obj.date])) {
                uni.msgBox("参数有误" + uni.hide("addDateTimePicker"));
                return;
            }
            panel = $(panel);
            var date = obj.date;
            var qz = $("#dlg_basic_dt_selecter");
            var para = obj;
            var horizon = type == "horizon" ? " .md_date" : "";
            var str = "";
            para.unit = "10"||"10";
            if (!obj.isAdd)
                panel.html("");//清空
            var picker;
            if (para.fix) {//固定时段
                $(".tmp_fix" + horizon, qz).each(function () { str += $(this).html(); });
                if (type == "horizon") str = "<tr>" + str + "</tr>";
                picker = $(str);
                var sel = $(".mt_fix_time", picker);
                var now=new Date();
                var today=now.format("yyyy-MM-dd")==date;
                var e=now.getHours()*100+now.getMinutes();
                for (var i = 0; i < obj.ops.length; i++) {
                    var op=obj.ops[i];
                    var start=op.start;
                    var end = op.end;
                    var flg = false;
                    if(today){
                        if(timeInt(end)<=e){
                            continue;
                        }
                        if(timeInt(start)<=e){
                            flg = true;
                    }
                    }
                    sel.append("<option value='" +date+" " +start + "&" +date+" "+ end + "'>" + (flg ? "现在" : start) + " - " + end + "</option>");
                }
                    var mt_start = picker.find(".mt_start");
                    var mt_end = picker.find(".mt_end");
                    sel.change(function () {
                        var v = $(this).val();
                        var tm = v.split("&");
                        if (tm.length == 2) {
                            mt_start.val(tm[0]);
                            mt_end.val(tm[1]);
                        }
                    });
                    sel.change();
            }
            else if (obj.allowLong) {//长期
                if ("1" == "1") {//整日
                    $(".tmp_date" + horizon, qz).each(function () { str += $(this).html(); });
                    if (type == "horizon") str = "<tr>" + str + "</tr>";
                    picker = $(str);
                    $(".mt_start_date", picker).val(obj.startDate || date);
                    dateSel($(".mt_end_date", picker), obj.startDate || date, obj.endDate);
                    $(".open_start", picker).val(obj.openStart);
                    $(".open_end", picker).val(obj.openEnd);
                    //multiTime();
                }
                else {//跨天
                    $(".tmp_datetime" + horizon, qz).each(function () { str += $(this).html(); });
                    if (type == "horizon") str = "<tr>" + str + "</tr>";
                    picker = $(str);
                    var mt_end = $(".mt_end_date", picker);
                    dateSel(mt_end, obj.startDate || date, obj.endDate);
                    $(".mt_start_time", picker).resvTimeClick($(".mt_end_time", picker), para, mt_end);
                    //multiTime();
                }
            }
            else if (obj.cycleDate) {//周期
                $(".tmp_cycledate" + horizon, qz).each(function () { str += $(this).html(); });
                if (type == "horizon") str = "<tr>" + str + "</tr>";
                picker = $(str);
                $(".set_cycle_date", picker).click(function () {
                    var pl = $("<div><table class='cycle_date_tbl'></table></div>");
                    var tp = {
                        stepMinute: obj.unit,
                        startDate: obj.startDate || date,
                        endDate: obj.endDate || date,
                        startTime: obj.start,
                        endTime: obj.end
                    };
                    pro.d.basic.cycleDateTimePicker($("table", pl), tp);
                    uni.dlg(pl, "周期时间选择", 680, 200, function (dlg) {
                        var rlt = pro.d.basic.analysisDateTime(dlg);
                        if (rlt) {
                            picker.find(".cycle_desc").html(rlt.desc);
                            picker.find(".cycle_start").val(rlt.start);
                            picker.find(".cycle_end").val(rlt.end);
                            picker.find(".calc_detail_date").removeAttr("disabled").click(function () {
                                var dts = rlt.date;
                                var str = "<strong>" + rlt.desc + "</strong><br/><br/>";
                                for (var i = 0; i < dts.length; i++)
                                    if (dts[i]) {
                                        var dt = uni.parseDate(dts[i]);
                                        str += dt.format("yyyy-MM-dd，星期E") + "<br/>";
                                    }
                                uni.msgBox(str, "详细日期");
                            });
                            $(dlg).dialog("close");
                        }
                    });
                });
            }
            else {//当日
                $(".tmp_time" + horizon, qz).each(function () { str += $(this).html(); });
                if (type == "horizon") str = "<tr>" + str + "</tr>";
                picker = $(str);
                $(".mt_start_time", picker).resvTimeClick($(".mt_end_time", picker), para);
                //multiTime();
            }
            $(".mt_date", picker).html(date);
            panel.append(picker);
            return picker;
            //function multiTime() {//多时段选择 必须水平样式
            //    if ("=GetConfig("allowMultiTime")" == "1" && type == "horizon") {
            //        if (obj.isAdd) {
            //            $(".add_picker", picker).remove();
            //        }
            //        else {
            //            $(".sub_picker", picker).remove();
            //            $(".add_picker", picker).click(function () {
            //                obj.isAdd = true;
            //                pro.d.basic.addDateTimePicker(panel, obj, type);
            //                obj.isAdd = false;
            //            });
            //        }
            //    }
            //    else {
            //        $(".sub_picker", picker).remove();
            //        $(".add_picker", picker).remove();
            //    }
            //}
        },
        //添加/维护成员
        mGroupMembers: function (panel, opt) {
            var qz = $("#dlg_basic_mb_add");
            if (opt && opt.md == "complex") {
                $(panel).html($(".tmp_complex", qz).html()).find(".set_group_mb").click(setStudents);
            }
            else {
                var gm = $(panel).html($(".tmp_simple", qz).html());
                $(".min_user", gm).val(opt.min);
                $(".max_user", gm).val(opt.max);
                var p = $(".dialog", gm);
                var ul = $(".ul_items", p);
                var mbList = $(".mb_list", gm);
                //var mbs = uni.getHash();//获取哈希表
                var pop = uni.pop(gm, {
                    con: p, orien: "right", colseBtn: false,except:[pro.acc.id], delItemFun: function (rlt) {
                        mbList.val(rlt.keys().join());
                    }
                });
                $(".mb_name_ipt", gm).procomplete(function (event, ui) {
                    debugger;
                    if (ui.item) {
                        if (ui.item.id && ui.item.id != "") {
                            //if (ui.item.szLogonName == pro.acc.id) { uni.msgBox("无需添加本人"); return; }
                            if (pop.items.size() == 0) pop.addItem(pro.acc.id,pro.acc.name);//默认加入本人
                            if (pop.items.size() < parseInt(opt.max))
                                mbList.val((pop.addItem(ui.item.szLogonName, ui.item.name)).keys().join());
                            else
                                uni.msgBox("组成员已满");
                        }
                    }
                });
            }
            //设置组
            function setStudents() {
                var pg_group = $(".group_id", panel);
                var para = uni.getObj(opt) || {};
                para.mb_accno = pro.acc.accno;
                if (pg_group.val()) {
                    para.group = pg_group.val();
                }
                parent.pro.d.group.manage('维护组成员', para, function (d) {
                    if (d.group_id) {//后台优先组号
                        pg_group.val(d.group_id);
                        $(".group_name", panel).html(d.group_name + "(<span class='red'>" + d.group_num + "</span>人)");
                    }
                    else if (d.mb_acc_list) {
                        pg_group.val('');
                        $(".mb_list", panel).val(d.mb_acc_list);
                        $(".group_name", panel).html(d.group_name + "(<span class='red'>" + d.group_num + "</span>人)");
                    }
                })
            }
        },
        //添加周期时间选择器
        cycleDateTimePicker: function (panel, para) {
            if (!para) para = {};
            var qz = $("#dlg_basic_cycle_dt");
            var tmp = $(panel).html($(".tmp_cycle", qz).html());
            //时间周期
            var cyc = $(".cycle_type", tmp);
            cyc.val(para.type || "d");//默认日
            cyc.change(function () {
                var pthis = $(this);
                var w = pthis.parent().find(".view_week").hide();
                var m = pthis.parent().find(".view_month").hide();
                if (pthis.val() == "w")
                    w.show();
                else if (pthis.val() == "m")
                    m.show();
            });
            cyc.trigger("change");
            //模式转换
            tmp.find(".cvt_single_day").click(function () {
                tmp.find(".single_hide").hide();
                tmp.find(".cycle_hide").show();
            });
            if (para.singleText)
                tmp.find(".cvt_single_day").html(para.singleText);
            tmp.find(".cvt_cycle_day").click(function () {
                tmp.find(".cycle_hide").hide();
                tmp.find(".single_hide").show();
            });
            if (para.cycleText)
                tmp.find(".cvt_cycle_day").html(para.cycleText);
            //选时控件
            var selDate = $(".sel_date", tmp);
            selDate.datepicker({
                minDate: 0
            });
            var selTime = $(".sel_time", tmp);
            if (selTime.timepicker) {
                selTime.timepicker({
                    controlType: 'select',
                    timeFormat: "HH:mm",
                    stepHour: para.stepHour || 1,
                    stepMinute: para.stepMinute || parseInt("10"||0),
                    hourMin: para.hourMin || 6,
                    hourMax: para.hourMax || 23
                });
            }
            //时间联动
            var tm_start = $(".time_start", tmp);
            var tm_end = $(".time_end", tmp);
            tm_start.change(function () {
                var sta=tm_start.val();
                var en = tm_end.val();
                if (sta) {
                    if (en) {
                        var i_sta = parseInt(sta.replace(":", ""));
                        var i_en = parseInt(en.replace(":", ""));
                        if (i_en < i_sta) tm_end.val(sta);
                    }
                    else
                        tm_end.val(sta);
                }
            });
            //初始化时间
            $(".date_start", tmp).val(para.startDate || "");
            $(".date_end", tmp).val(para.endDate || "");
            $(".time_start", tmp).val(para.startTime || "");
            $(".time_end", tmp).val(para.endTime || "");
            if (para.weeks && cyc.val() == "w") {//周
                $(".cycle_week", tmp).each(function () {
                    var pthis = $(this);
                    if (uni.isInArray(pthis.val(), para.weeks))
                        pthis.attr("checked", true);
                });
            }
            if (para.day && cyc.val() == "m") {//月
                $(".cycle_day", tmp).val(para.day);
            }
            //频率
            $(".cycle_freq", tmp).val(para.freq || "1");//默认1
            //计算详细日期
            $(".cmp_detail", tmp).click(function () {
                var rlt = pro.d.basic.analysisDateTime(tmp);
                if (rlt) {
                    var dts = rlt.date;
                    var str = "<strong>" + rlt.desc + "</strong><br/><br/>------------------------<br/>";
                    for (var i = 0; i < dts.length; i++) {
                        if (dts[i]) {
                            var dt = uni.parseDate(dts[i]);
                            str += dt.format("yyyy-MM-dd，星期E") + "<br/>";
                        }
                    }
                    uni.msgBox(str, "详细日期");
                }
            });
            //默认模式
            if (para.dftM == "single")
                tmp.find(".cvt_single_day").trigger("click");
            else
                tmp.find(".cvt_cycle_day").trigger("click");
        },
        //周期时间选择器 计算周期时间
        analysisDateTime: function (info) {
            info = $(info);
            if (!$(info).mustItem()) return false;
            //取值
            var d_start = $(".date_start", info).val();
            var d_end = $(".date_end", info).val();
            var t_start = $(".time_start", info).val();
            var t_end = $(".time_end", info).val();
            var type = $(".cycle_type", info).val();
            var freq = parseInt($(".cycle_freq", info).val());
            var ws = $(".cycle_week:checked", info);
            var d = parseInt($(".cycle_day", info).val() || 0);
            if (uni.compareDate(uni.parseDate(d_start + " " + t_start), new Date(), "m") <= 0) { uni.msgBox("所选时间不能早于当前时间"); return false; }
            //单日模式
            if (info.find(".cycle_hide").is(":visible")) {
                return { start: [d_start + " " + t_start], end: [d_start + " " + t_end], desc: d_start + " " + t_start+"-"+t_end, date: [d_start], startTime: t_start, endTime: t_end, startDate: d_start, endDate: d_start, type: "d", freq: 1 };
            }
            //检查周次
            if (type == "w" && ws.length == 0) { uni.msgBox("至少勾选一个周次"); return false; }
            //初始值
            var rlt = { start: [], end: [], desc: "", date: [], startTime: t_start, endTime: t_end, startDate: d_start, endDate: d_end, weeks: [], day: d, type: type, freq: freq };
            //
            rlt.desc = d_start + "至" + d_end + "," + t_start + "-" + t_end;
            var dstart = uni.parseDate(d_start);
            var dend = uni.parseDate(d_end);
            var dt = uni.parseDate(d_start);
            var today = new Date();
            if (uni.compareDate(dt, today) < 0) dt = today;
            var len = uni.compareDate(dend, dt);
            if (len > 366) len = 366;//防止恶意
            if (type == "d") {
                rlt.desc += "(每" + freq + "天)";
                for (var i = 0; i <= len; i += freq) {
                    var fmt = dt.format("yyyy-MM-dd");
                    rlt.date.push(fmt);
                    rlt.start.push(fmt + " " + t_start);
                    rlt.end.push(fmt + " " + t_end);
                    dt.addDays(freq);
                }
            }
            else if (type == "w") {
                var chi = ["日", "一", "二", "三", "四", "五", "六"];
                rlt.desc += "(每" + freq + "周,星期";
                for (var k = 0; k < ws.length; k++) {
                    var w = parseInt(ws[k].value);
                    rlt.weeks.push(w);
                    rlt.desc += (k == 0 ? "" : "/") + chi[w];
                }
                for (var i = 0; i <= len; i++) {
                    if (uni.isInArray(dt.getDay(), rlt.weeks)) {
                        fmt = dt.format("yyyy-MM-dd");
                        rlt.date.push(fmt);
                        rlt.start.push(fmt + " " + t_start);
                        rlt.end.push(fmt + " " + t_end);
                        if (dt.getDay() == rlt.weeks[rlt.weeks.length - 1]) {
                            dt.addDays(7 * (freq - 1));
                            i += 7 * (freq - 1);
                        }
                    }
                    dt.addDays(1);
                }

                rlt.desc += ")";
            }
            else if (type == "m") {
                rlt.desc += "(每" + freq + "月," + d + "日)";
                dt.setDate(d);
                if (uni.compareDate(dt, dstart) < 0) dt.addMonths(1);
                while (uni.compareDate(dt, dend) <= 0) {
                    fmt = dt.format("yyyy-MM-dd");
                    rlt.date.push(fmt);
                    rlt.start.push(fmt + " " + t_start);
                    rlt.end.push(fmt + " " + t_end);
                    dt.addMonths(freq);
                }
            }
            if (rlt.date.length > 0)
                return rlt;
            else {
                uni.msgBox("未取到任何有效的日期");
                return false;
            }
        }
    }
</script>
<style>
    .dialog .ul_items li { min-width: 200px; line-height: 20px; height: 22px; font-size: 12px; background: #BFE5F0; border: 1px solid #eee; margin: 1px; padding: 1px 2px; position: relative; color: #666; overflow: hidden; }
    .dialog .ul_items li .del { font-size: 16px; font-weight: bold; position: absolute; top: 1px; right: 2px; color: #000; opacity: .2; background: #BFE5F0; }
    .dialog .cycle_date_tbl { width: 100%; }
    .dialog .cycle_date_tbl tr td { vertical-align: middle; height: 46px; }
    .dialog .cycle_date_tbl tr td:first-child { width: 87px; }
    .dialog .cycle_date_tbl .sel_time { width: 60px; }
    .dialog .cycle_date_tbl select, .dialog .cycle_date_tbl input[type=text] { height: 28px; }
</style>

        
    <script type="text/javascript">
        var acc = {};
        acc.id = "10132510139";
        acc.accno = "9760293";
        acc.name = "陈正宇";
        acc.phone = $.trim("18701901620");
        acc.msn = "";
        acc.email = $.trim("");
        acc.ident = "4194561";
        acc.dept = "软件学院";
        acc.tutor = "";
        acc.tutorid = "";
        acc.tsta = "";
        acc.rtsta = "";
        acc.score = "200";
        acc.credit = [["研究室惩罚规则","200","300",""]];
        acc.pro = "";
        acc.role = "134217730";
        pro.acc = acc;
    </script>

        
<script>
    var term = {};
    term.year="";
    term.name="";
    term.status = "";
    term.start = "";
    term.end = "";
    term.firstweek = 0;
    term.totalweek = 0;
    term.secnum = 0;
    term.cts1 = "";
    term.cts1start = "";
    term.cts1end = "";
    term.cts2 = "";
    term.cts2start = "";
    term.cts2end = "";
    pro.term = term;
</script>
        
<div style="display: none;">
    <!--注册账户-->
    <div id="dlg_regist_acc" class="dialog">
        <form class="dlg_lg_validate" onsubmit="return false;">
            <p class="intro tag"></p>
            <div>
                <table style="margin: 20px 5px 0 5px;">
                    <tbody>
                        <tr>
                            <td>帐号 </td>
                            <td>
                                <input type="text" id="regist_acc_id" maxlength="16" class=" validate[required,maxSize[16]],custom[onlyLetterNumber],ajax[ajaxIdIsExistFail]]" name="id" /></td>
                            <td><span style="color: red;">*</span>&nbsp数字与字母，最多16位</td>
                        </tr>
                        <tr>
                            <td>密码 </td>
                            <td>
                                <input type="password" id="regist_acc_pwd" maxlength="14" class=" validate[required,maxSize[14]]" name="pwd" /></td>
                            <td><span style="color: red;">*</span>&nbsp最多14位</td>
                        </tr>
                        <tr>
                            <td>密码确认 &nbsp</td>
                            <td>
                                <input type="password" id="regist_acc_pwd_r" class=" validate[required,equals[regist_acc_pwd]]" /></td>
                            <td><span style="color: red;">*</span></td>
                        </tr>
                        <tr>
                            <td>身份证号 &nbsp</td>
                            <td>
                                <input type="text" id="regist_acc_id_card" class=" validate[required,funcCall[chkIDCard]]" name="id_card" /></td>
                            <td><span style="color: red;">*</span>&nbsp必须真实，字母大写</td>
                        </tr>
                        <tr>
                            <td>真实姓名 &nbsp</td>
                            <td>
                                <input type="text" id="regist_acc_name" maxlength="14" class=" validate[required,maxSize[14]]" name="name" /></td>
                            <td><span style="color: red;">*</span></td>
                        </tr>
                        <tr>
                            <td>单位 </td>
                            <td>
                                <input type="text" id="regist_acc_dept" maxlength="18" class=" validate[required,maxSize[18]]" name="dept" /></td>
                            <td><span style="color: red;">*</span></td>
                        </tr>
                        <tr>
                            <td>部门 </td>
                            <td>
                                <input type="text" id="regist_acc_cls" maxlength="18" class=" validate[required,maxSize[18]]" name="cls" /></td>
                            <td><span style="color: red;">*</span></td>
                        </tr>
                        <tr>
                            <td>手机 </td>
                            <td>
                                <input type="text" id="regist_acc_phone" class=" validate[required,custom[phone]]" name="phone" /></td>
                            <td><span style="color: red;">*</span>&nbsp短信通知需要</td>
                        </tr>
                        <tr>
                            <td>邮箱 </td>
                            <td>
                                <input type="text" id="regist_acc_email" class=" validate[required,custom[email]]" name="email" /></td>
                            <td><span style="color: red;">*</span>&nbsp邮件通知需要</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <script type="text/javascript">
            </script>
        </form>
    </div>
    <!--激活账户-->
    <div id="dlg_act_acc" class="dialog" style="overflow: visible;">
        <form class="dlg_lg_validate" onsubmit="return false;">
            <p class="intro tag"></p>
            <div class="list">
                <table>
                    <tbody>
                        <tr>
                            <td>帐号 </td>
                            <td>
                                <input type="text" maxlength="16" class=" validate[required,maxSize[16]],ajax[ajaxIdIsRegisterOK]]" name="id" /></td>
                            <td><span style="color: red;">*</span>学号/工号</td>
                        </tr>
                        <tr>
                            <td>密码 </td>
                            <td>
                                <input type="password" name="pwd" /></td>
                            <td><span style="color: red;">*</span>同一卡通密码</td>
                        </tr>
                        <tr>
                            <td>手机 </td>
                            <td>
                                <input type="text" class=" validate[required,custom[phone]]" name="phone" /></td>
                            <td><span style="color: red;">*</span>&nbsp短信通知需要</td>
                        </tr>
                        <tr>
                            <td>邮箱 </td>
                            <td>
                                <input type="text" class=" validate[required,custom[email]]" name="email" /></td>
                            <td><span style="color: red;">*</span>&nbsp邮件通知需要</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <script type="text/javascript">
            </script>
        </form>
    </div>
    <div id="dlg_act_acc_simple" class="dialog" style="overflow: visible;">
        <form class="dlg_lg_validate" onsubmit="return false;">
            <div class="list">
                <table>
                    <tbody>
                        <tr>
                            <td>手机 </td>
                            <td>
                                <input type="text" class="phone validate[required,custom[phone]]" name="phone" /></td>
                            <td><span style="color: red;">*</span>&nbsp短信通知需要</td>
                        </tr>
                        <tr>
                            <td>邮箱 </td>
                            <td>
                                <input type="text" class="email validate[required,custom[email]]" name="email" /></td>
                            <td><span style="color: red;">*</span>&nbsp邮件通知需要</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </form>
    </div>
    <!--账户登录-->
    <div id="dlg_login" class="dialog">
        <form class="dlg_lg_validate" onsubmit="return false;">
            <div style="min-width: 300px;" class="lg_form">
                <div class="intro tag"></div>
                <div class="list">
                    <table>
                        <tbody>
                            <tr>
                                <td><span class="uni_trans">帐号</span> </td>
                                <td>
                                    <input type="text" maxlength="16" name="id" /></td>
                                <td><span class="id_intro hint_intro">学号/工号</span></td>
                            </tr>
                            <tr>
                                <td><span class="uni_trans">密码</span> </td>
                                <td>
                                    <input type="password" name="pwd" /></td>
                                <td><span class="pwd_intro hint_intro">同一卡通密码</span></td>
                            </tr>
                            
                            <tr>
                                <td></td>
                                <td>
                                    <label style="cursor: pointer;">
                                        <input type="checkbox" class="save_pwd_ck" />
                                        记住密码</label>
                                </td>
                            </tr>
                            
                        </tbody>
                    </table>
                </div>
                <div class="operate">
                    <input type="button" class="button default btn btn-info" value="登录" priority="9" onclick="$(this).parents('form:first').submit();" />
                    <input type="button" class="user_active button btn btn-warning" style="display: none" value="新用户激活" />
                </div>
            </div>

            <div class="intro_detail" style="float: left; width: 300px; border-left: 1px dotted #ddd; padding-left: 10px; margin-top: 5px;">
                
                
                
            </div>

        </form>
    </div>
</div>
<script type="text/javascript">

    //注册账户
    pro.d.lg.registAcc = function (suc, fail, intro) {
        var dlg = $("#dlg_regist_acc");
        var str = "▪ " + (intro || "请根据提示信息完成注册。");
        $(".intro", dlg).html(str);
        $("form:first", dlg).validationEngine({
            onValidationComplete: function (f, ret) {
                if (ret) {
                    pro.j.lg.fLogin("regist_acc", f, suc, fail);
                }
            }
        });
        uni.dlg(dlg, "用户注册", 460, 420, function (d, f) {
            $(f).submit();
        });
    }
    //用户激活
    pro.d.lg.actAcc = function (suc, fail, intro) {
        var dlg = $("#dlg_act_acc");
        var str = intro || "预约过程中，系统将通过您提供的联系方式发送反馈信息。";
        $(".intro", dlg).html(str);
        $("form:first", dlg).validationEngine({
            onValidationComplete: function (f, ret) {
                if (ret) {
                    pro.j.lg.fLogin("act", f, suc || function () { uni.msgBox("激活成功"); location.reload(); }, fail);//全页面刷新
                }
            }
        });
        uni.dlg(dlg, "用户激活", 420, 400, function (d, f) {
            $(f).submit();
        });
    }
    //用户登录
    pro.d.lg.login = function (suc, fail, intro) {
        var dlg = $("#dlg_login");
        //侧边提示
        var width = 420;
        var detail = $(".intro_detail");
        if ($.trim(detail.html()) == "") { detail.hide(); $(".hint_intro", dlg).show(); }
        else { detail.show(); width += 240; $(".lg_form", dlg).css("float", "left"); $(".hint_intro", dlg).hide(); }
        //头部提示
        var str = intro || "";
            $(".intro", dlg).html(str);
            //保存密码
            var isSV = "1" == "1";
            var svk = $(".save_pwd_ck", dlg);
            if ($.cookie("is_save_pwd") == "true") {
                svk.attr("checked", "checked");
            }
            var ipt_id = $("input[name=id]", dlg);
            var ipt_pwd = $("input[name=pwd]", dlg);
            if (isSV) {
                if (svk.is(':checked')) {
                    ipt_id.val($.cookie("pc_user") || "");
                    ipt_pwd.val($.cookie("pc_pwd") || "");
                }
                else {
                    $.cookie("pc_user", null);
                    $.cookie("pc_pwd", null);
                }
            }
            //事件注册
            if (!dlg.hasClass("dlg_inited")) {
                debugger;
                dlg.addClass("dlg_inited");
                if (isSV) {
                    svk.change(function () {
                        if (svk.is(':checked')) {
                            $.cookie("is_save_pwd", "true", { expires: 30 });
                        }
                        else {
                            $.cookie("is_save_pwd", null);
                        }
                    });
                }
                $("form:first", dlg).validationEngine({
                    onValidationComplete: function (f, ret) {
                        if (ret) {
                            var verif = $(".verif_number", f)
                            pro.j.lg.fLogin(verif.length > 0 ? "dlogin" : "login", f, function (rlt) {
                                if (rlt.ret == 2)
                                    uni.msgBox(rlt.msg, "", function () { location.reload(); })//$(".user_active", dlg).trigger("click"); 
                                else if (rlt.ret == 3) {
                                    uni.msgBox("微信未绑定", "", function () { location.reload(); });//微信绑定扫描二维码的特殊性，只能重登录检查
                                }
                                else {
                                    if (isSV && svk.is(':checked')) {
                                        $.cookie("pc_user", ipt_id.val(), { expires: 30 });
                                        $.cookie("pc_pwd", ipt_pwd.val(), { expires: 365 });
                                    }
                                    if (typeof (suc) == "function") {
                                        suc(rlt, dlg);
                                    }
                                    else
                                        location.reload();
                                }
                            }, function (rlt) {
                                if (verif.length > 0) {
                                    var img = $(".verif_img", f)[0];
                                    img.src = img.src + "?";
                                    verif.val("");
                                }
                                if (fail) fail(rlt);
                                else uni.msgBox(rlt.msg);
                            });
                        }
                    }
                });
            }
            if ($(".verif_img", dlg).length > 0) {//刷新验证码
                var img = $(".verif_img", dlg)[0];
                img.src = img.src + "?";
            }
            uni.dlg(dlg, "用户登录", width, 200);
        }
        $(function () {
            $("#dlg_login .user_active").click(function () {
                $("#dlg_act_acc input[name=id]").val($("#dlg_login input[name=id]").val());
                $("#dlg_act_acc input[name=pwd]").val($("#dlg_login input[name=pwd]").val());
            });
            //按钮事件
            $("a.login,span.login").click(function () {
                pro.d.lg.login();
            });
            $("a.user_active,span.user_active,input.user_active").click(function () {
                pro.d.lg.actAcc();
            });
            //检查微信绑定
            if ("0" == "1" && pro.isLogin() && !pro.acc.msn) {
            var qr = '';
            var img = "<span>请使用微信扫二维码，绑定微信</span><div class='dft_qr_code'><img alt='' style='width:200px;height:200px;' src='" + qr + (qr.indexOf('?') < 0 ? "?" : "&") + "ID=" + pro.acc.id + "&session=2556053010'/></div>";
            uni.msgBox(img, "微信绑定", function () { pro.j.lg.initAcc(function () { if (!pro.acc.msn) { location.reload(); } else { uni.msgBox("绑定微信成功"); } }); });
        }
        //检查联系方式信息
        if ("False".toLowerCase() == "true" && pro.isLogin() && (!pro.acc.phone || !pro.acc.email)) {
            var dlg = $("#dlg_act_acc_simple");
            var phone = dlg.find(".phone");
            var email = dlg.find(".email");
            phone.val(pro.acc.phone || "");
            email.val(pro.acc.email || "");
            $("form:first", dlg).validationEngine({
                onValidationComplete: function (f, ret) {
                    if (ret) {
                        pro.j.acc.upContact(phone.val(), email.val(), function () { uni.msgBox("激活成功", "", function () { location.reload(); }); });
                    }
                }
            });
            uni.dlg(dlg, "用户激活", 420, 200, function (d, f) {
                $(f).submit();
            }, null, function () { pro.j.lg.logout(); });
        }
    });
</script>

        <div class="back_top"></div>
    </div>
    <header class="navbar navbar-inverse navbar-static-top" role="banner" style="">
        <div class="container" id="top_nav">
            <nav class="collapse navbar-collapse bs-navbar-collapse" role="navigation">
                <h4 class="pull-left" style="font-size: 24px;">IC空间管理系统</h4>
                <ul class="nav navbar-nav navbar-right">
                    <li style="display:none;" class="lang_set">
                        <img src="../a/theme/images/zh_version.gif" alt="中文" data-lang="zh-cn"/><img src="../a/theme/images/en_version.gif" alt="English" data-lang="en-gb"/>
                    </li>
                    <li  style="display:"><a href="../../../pages/default.aspx">[管理端]</a></li>
                    <li class="user_info">
                        <span class="login_hide" style="">预约请登录！</span>
                        <span class="login_show"><span class="glyphicon glyphicon-user"></span>&nbsp;您好,陈正宇</span>
                    </li>
                    <li style="" class="logout lg_act login_show">
                        <a><span>退出<span class="glyphicon glyphicon-log-out"></span></span></a>
                    </li>
                    <li style="" class="login lg_act login_hide" onclick="pro.d.lg.login();">
                        <a><span>登录<span class="glyphicon glyphicon-log-in"></span></span></a>
                    </li>
                </ul>
            </nav>
        </div>
        <script>
            var url = location.href.toLowerCase();
            var list = $("#top_nav").find("a");
            list.each(function (i) {
                var pthis = $(this);
                var href = pthis.attr("href");
                if (href)
                    href = href.toLowerCase();
                if (!uni.isNull(href)) {
                    if (url.indexOf(href) > 0) {
                        pthis.parent("li").addClass("active");
                    }
                    else {
                        pthis.parent("li").removeClass("active");
                    }
                }
            });
        </script>
    </header>
    <div id="jumbotron" class="">
        <div class="container acc_info">
            <h3 class="text-right"><span class="glyphicon glyphicon-user"></span>&nbsp;您好,<span class="acc_info_name">陈正宇</span>  <span style="font-size: 14px;">欢迎使用IC空间管理系统！</span></h3>
            <p style="border-top: 1px solid #fff; font-size: 14px; padding: 3px 5px;text-align:right;margin: 0;"><span class="login_show" style="">登录名：<span class="acc_info_id">10132510139</span> |  部门：<span class="acc_info_dept">软件学院</span></span><span class="login_hide" style="">预约请登录！</span></p>
        </div>
    </div>

    <div class="container">
        

    <input type="hidden" value="" class="dft_close_devcls" />
    <div class="row con_top">
        <img style="height: 140px; width: 100%;" src="theme/images/index.jpg" class="hidden" />
        <table class="struct_tbl">
            <tbody>
                <tr>
                    <td class="left_panel">
                        <div class="col">
                            <div id="info_tree">
                                <div style="width: 263px;">
                                    <div url="index.aspx" con="#detail_con" class="click_load click">
                                        <img style="height: 100px; width: 100%; display: none" src="theme/images/logo.jpg" />
                                        <h3>
                                            <a id="home" class="home"><span class="glyphicon glyphicon-home"></span>&nbsp;主页&nbsp;</a>
                                        </h3>
                                    </div>
                                    <div class="line"></div>
                                    <ul class="nav oth_list">
                                        <li><a url="../a/article.aspx?id=help&type=other" con="#detail_con" class="click_load"><span><span class="glyphicon glyphicon-question-sign"></span>&nbsp;使用帮助</span></a></li>
                                        <li class="login_show" style=""><a id="user_center" url="../a/center.aspx" con="#detail_con" class="click_load"><span><span class="glyphicon glyphicon-user"></span>&nbsp;个人中心</span></a></li>
                                        <li style="display: none"><a url="../a/openatycenter.aspx?type=pre" con="#detail_con" class="click_load"><span><span class="glyphicon glyphicon-bookmark"></span>&nbsp;活动预告</span></a></li>
                                        <li style="display: none"><a url="../a/openatycenter.aspx?type=old" con="#detail_con" class="click_load"><span><span class="glyphicon glyphicon-bookmark"></span>&nbsp;活动回顾</span></a></li>
                                        <li class="login_show" style="display:none"><a url="../a/castvote.aspx" con="#detail_con" class="click_load"><span><span class="glyphicon glyphicon-signal"></span>&nbsp;网上投票</span></a></li>
                                    <!--    <li style=""><a href="../../../pages/default.aspx"><span class="glyphicon glyphicon-bookmark"></span>&nbsp;返回图书馆主页</a></li>-->
                                    </ul>
                                    <div class="line"></div>
                                    <div id="item_list">
                                        <h4><span class="glyphicon glyphicon-list" style="width: 18px;"></span>&nbsp;资源列表</h4>
                                        <ul class="it_cls_list nav">
                                            <h5>空间</h5><li class='nav_cls_li'><ul class='it_list nav'><li class='it' it='devcls' url="../a/dftdetail.aspx?classKind=1&id=1677879&name=%e9%97%b5%e8%a1%8c%e5%bd%b1%e8%a7%86%e6%ac%a3%e8%b5%8f%e5%ae%a4"><a><span>闵行影视欣赏室</span></a></li><li class='it' it='devcls' url="../a/dftdetail.aspx?classKind=1&id=3674968&name=%e4%b8%ad%e5%8c%97%e7%a0%94%e7%a9%b6%e5%ae%a4%ef%bc%88%e7%8e%bb%e7%92%83%e9%97%a8%ef%bc%89"><a><span>中北研究室（玻璃门）</span></a></li><li class='it' it='devcls' url="../a/dftdetail.aspx?classKind=1&id=3675132&name=%e4%b8%ad%e5%8c%97%e7%a0%94%e7%a9%b6%e5%ae%a4%ef%bc%88%e6%9c%a8%e9%97%a8%ef%bc%89"><a><span>中北研究室（木门）</span></a></li><li class='it' it='devcls' url="../a/dftdetail.aspx?classKind=1&id=3675178&name=%e4%b8%ad%e5%8c%97%e4%b8%ad%e5%9e%8b%e7%a0%94%e8%ae%a8%e5%ae%a4"><a><span>中北中型研讨室</span></a></li><li class='it' it='devcls' url="../a/dftdetail.aspx?classKind=1&id=5112601&name=%e4%b8%ad%e5%8c%97%e4%b8%89%e6%a5%bc%e6%95%99%e5%b8%88%e7%a0%94%e7%a9%b6%e5%ae%a4"><a><span>中北三楼教师研究室</span></a></li><li class='it' it='devcls' url="../a/dftdetail.aspx?classKind=1&id=5117985&name=%e4%b8%ad%e5%8c%97%e6%95%99%e5%b8%88%e7%a0%94%e8%ae%a8%e5%ae%a4"><a><span>中北教师研讨室</span></a></li><li class='it' it='devcls' url="../a/dftdetail.aspx?classKind=1&id=42498453&name=%e9%97%b5%e8%a1%8c%e6%95%99%e5%b8%88%e7%a0%94%e7%a9%b6%e5%ae%a4"><a><span>闵行教师研究室</span></a></li><li class='it' it='devcls' url="../a/dftdetail.aspx?classKind=1&id=11562&name=%e9%97%b5%e8%a1%8c%e7%a0%94%e7%a9%b6%e5%ae%a4"><a><span>闵行研究室</span></a></li><li class='it' it='devcls' url="../a/dftdetail.aspx?classKind=1&id=11650&name=%e9%97%b5%e8%a1%8c%e5%b0%8f%e7%a0%94%e8%ae%a8%e5%ae%a4"><a><span>闵行小研讨室</span></a></li><li class='it' it='devcls' url="../a/dftdetail.aspx?classKind=1&id=11680&name=%e9%97%b5%e8%a1%8c%e5%a4%a7%e7%a0%94%e8%ae%a8%e5%ae%a4"><a><span>闵行大研讨室</span></a></li><li class='it' it='devcls' url="../a/dftdetail.aspx?classKind=1&id=3675214&name=%e4%b8%ad%e5%8c%97%e5%a4%a7%e5%9e%8b%e7%a0%94%e8%ae%a8%e5%ae%a4"><a><span>中北大型研讨室</span></a></li><li class='it' it='devcls' url="../a/dftdetail.aspx?classKind=1&id=4251118&name=%e5%92%96%e5%95%a1%e5%8e%85"><a><span>咖啡厅</span></a></li></ul></li>
                                        </ul>
                                        <script type="text/javascript">
                                            treeFiler();
                                        </script>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </td>
                    <td>
                        <div id="panel_right" class="col">
                            <div style="background: left no-repeat url(theme/images/index_01.jpg); height: 80px; width: 100%; border-radius: 6px;" class="hidden"></div>
                            <div id="detail_con" style="display: none;"></div>
                            <div id="cache_con" style="display: none;"></div>
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>

    </div>
    <footer class="bs-docs-footer" role="contentinfo">
        <div class="container">
            <div class="footer_other_info"></div>
            版权所有：IC空间管理系统
            <div class="hidden" name="当前异步加载的网页"><span class="by_hr_load"></span></div>
        </div>
    </footer>
</body>
</html>
