
<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<body>
    <form name="ctl00" method="post" action="dftdetail.aspx?classKind=1&amp;id=3675132&amp;name=%u4e2d%u5317%u7814%u7a76%u5ba4%uff08%u6728%u95e8%uff09" id="ctl00">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUKLTE2NDA0NzMwM2RkNPJOLVFlOYTvWqzYBJAUJZeC0gM=" />

        <input name="classKind" type="hidden" id="classKind" class="class_kind" value="1" />
        <input name="infoId" type="hidden" id="infoId" class="info_id" value="3675132" />
        <input name="infoName" type="hidden" id="infoName" class="info_name" value="中北研究室（木门）" />
    
<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEWBALevo+jDALbmOTqDgLy3+/MCwKs8MqTCmKThA7XxKeN0SjDUSnVpe27Jp6t" /></form>
    <div>
        <div class="click btn_back" onclick="uni.hr.back();" style="display: none"><span class="glyphicon glyphicon-chevron-left"></span>&nbsp;<span class="uni_trans">返回</span></div>
        <div>
            <h1 class="h_title">中北研究室（木门）</h1>
            <div style="margin: 10px; margin-bottom: 20px; overflow: hidden;">
                <p><img src="../../upload/info/upload/2015-07-11/MM12.130810589120171250.jpg" title="MM12.jpg"/></p>
            </div>
        </div>
        <div class="info_unitab">
            <ul class="tab_head">
                <li>
                    <div class="title">预约状态</div>
                    <div class="caret"></div>
                </li>
                <li class="title">
                    <div class="title">预约须知</div>
                    <div class="caret"></div>
                </li>
                <li>
                    <div class="title">硬件配置</div>
                    <div class="caret"></div>
                </li>
                <li>
                    <div class="title">相册展示</div>
                    <div class="caret"></div>
                </li>
               
            </ul>
            <div class="tab_con">
                <div class="cld-obj-detail" onselectstart="return false">
                    <code>拖拽选择时间</code>
                    
<div class="dlg_resv_panel_group" onselect="return false;">
    <div class="resv_panel dialog" id="dlg_resv_panel_default_636828365424843750">
        <div class="div_remark remark">
        </div>
        <div class="rsv_state_slider" style="margin: 0 5px;"></div>
        <form onsubmit="return false;" class="list">
            <div>
                <input type="hidden" class="dev_id" name="dev_id" />
                <input type="hidden" class="lab_id" name="lab_id" />
                <input type="hidden" class="kind_id" name="kind_id" />
                <input type="hidden" class="room_id" name="room_id" />
                <input type="hidden" class="type" name="type" value="dev" />
                <input type="hidden" class="prop" name="prop" />
                <input type="hidden" class="test_id" name="test_id" />
                <input type="hidden" class="term" name="term" />
                <table>
                    <tbody>
                        <tr>
                            <td><span class="uni_trans">申请信息</span></td>
                            <td>
                                <span class="rsv_obj_name"></span>，<span class="uni_trans">申请人</span>：<span class="apply_people"></span>
                            </td>
                        </tr>
                        
                        <tr class="tr_theme hidden">
                            <td><span class="name_theme uni_trans">主题</span></td>
                            <td>
                                
                                <input type="text" name="test_name" class="con_theme " data-msg="必填内容不允许为空" style="width: 233px;" maxlength="32" />
                                
                            </td>
                        </tr>
                        <tr class="md_group">
                            <td><span class="uni_trans">成员</span></td>
                            <td class="dlg_mb_panel"></td>
                        </tr>
                    </tbody>
                    <tbody class="dlg_dt_panel">
                    </tbody>
                    <tbody>
                        <tr class="resv_fee_panel hidden">
                            <td><span class="uni_trans">费用</span></td>
                            <td><span class="uni_trans">单价：</span><span class="unit_price"></span>；
                                <span class="uni_trans">总计：</span><span class="total_price"></span></td>
                        </tr>
                        <tr class="file_up_panel" style="font-size: 12px;">
                            <td><span class="uni_trans">申请报告</span></td>
                            <td>
                                <div style="text-decoration: underline; line-height: 20px; display: none"><a href=""><span class="uni_trans">下载申请报告模版</span></a><span class="red">*</span></div>
                                <div style="overflow: hidden;" class="up_file_panel">
                                    <div class="choice_file_panel"></div>
                                    <div class="btn-group">
                                        <button type="button" class="upload_file btn btn-info"><span class="uni_trans">上传</span></button><input type='hidden' name='up_file' />
                                        <button type="button" class="cur_file_name btn btn-default" style="max-width: 230px;" disabled></button>
                                    </div>
                                </div>
                            </td>
                        </tr>
                        <tr class="date_flag hidden">
                            <td><span class="uni_trans">申请说明</span></td>
                            <td>
                                <div class="uni_trans" style="line-height: 18px;">其它备注信息，请填入此输入框 (45)</div>
                                <textarea rows="4" name="memo" style="width: 260px; line-height: 20px;" class="memo  " data-msg="申请说明必须填写" maxlength="45"></textarea>
                            </td>
                        </tr>
                        
                    </tbody>
                </table>
            </div>
            <div class="submitarea">
                <input type="button" class="btn btn-info mt_sub_resv" value="提交" />
                <input type="button" class="dlg_close btn btn-default" value="返回" />
            </div>
        </form>
    </div>
</div>
<script>
    (function () {
        var calendar_para = {};//calendar私有公共参数
        if (typeof (uni_calendar_dft_opt) != "object") uni_calendar_dft_opt = {};//外部配置
        var idlg = $("#dlg_resv_panel_default_636828365424843750");//公共dlg对象
        $(function () {
            var disable = "";
            if (disable == "true") return;//停止初始化
            //解析参数
            var req = uni.getReq();
            var purl = uni.getObj(uni_calendar_dft_opt);
            //过滤掉函数
            for (var key in purl) {
                if (typeof (purl[key]) == "function") purl[key] = null;
            }
            //
            calendar_para.src_type = "cls";
            calendar_para.classkind = purl.classkind = req["classKind"] || "1" || purl.classkind;
            calendar_para.test_id = purl.test_id = req["testId"] || purl.test_id;//教学实验项目号
            calendar_para.term = purl.term = req["term"] || purl.term;//教学学期
            calendar_para.display = purl.display = req["display"] || purl.display || "cld";
            purl.islong = req["isLong"] || "" || purl.islong;
            var alone = req["alone"] || "false";
            if (alone == "true") purl.alone = true;
            purl.iskind = req["isKind"] || "" || purl.iskind;
            purl.md = purl.md || ((purl.islong || "").toLowerCase() == "true" ? "m" : "d");
            purl.class_id = req["classId"] || "3675132" || purl.class_id;
            purl.lab_id = req["labId"] || "" || purl.lab_id;
            purl.kind_id = req["kindId"] || "" || purl.kind_id;
            purl.room_id = req["roomId"] || "" || purl.room_id;
            purl.dev_id = req["dev"] || "" || purl.dev_id;
            purl.operate = req["operate"] || purl.operate;
            purl.purpose = purl.purpose || "";
            var selDate = req["click"] == "false" ? undefined : SelDateTime;
            var width = parseInt(req["w"] || "" || "840");
            purl.img = req["img"] || "" || purl.img;
            purl.cld_name = purl.cld_name || "default";//状态控件名
            //获取实例
            var panel = $("#calendar_636828365424843750");
            panel.attr("name", purl.cld_name);
            var calendar;
            //载入状态控件
            function loadCld(filter) {
                var kvp = uni.getObj(purl);
                if (filter && typeof (filter) == "object") $.extend(true, kvp, filter);
                //不需要传的值
                delete kvp.img;
                //
                if (kvp.display == "fp") {//平面图
                    calendar = panel.uniFloorPlan({
                        width: width,
                        img: purl.img,
                        allDay: (parseInt("0") & parseInt(calendar_para.classkind))>0,
                        step: parseInt("10" || 10),
                        interval: parseInt("60,120" || 60),
                        isEdit: (pro.isLogin() && (parseInt(pro.acc.ident) & 268435456) > 0),
                        evInit: function (callback) {
                            pro.j.dev.getDevCoord(kvp, function (rlt) {
                                callback(rlt);
                            });
                        },
                        evSelDot: selDate,
                        evUpTime: function (date, start, end, callback) {
                            var pra = kvp || {};
                            pra.date = date;
                            if (start && end) {
                                pra.fr_start = start;
                                pra.fr_end = end;
                            }
                            else {
                                pra.fr_all_day="true";
                            }
                            pro.j.dev.getRsvSta(pra, function (rlt) {
                                var list = rlt.data;
                                callback(list, "unilab3", { showClose: ("1" == "1" ? true : false) });
                            });
                        },
                        evSaveCoorb: function (para, boxs, callback) {
                            var str = para.width + "&" + para.height + "&" + para.istitle;
                            var list = boxs.values();
                            $.each(list, function () {
                                str += "&" + this.key + "," + this.css("top") + "," + this.css("left") + "," + this.sz;
                            });
                            pro.j.dev.setDevCoord(kvp, str, callback);
                        },
                        evFinish: function (fp) {
                            var search = $(fp).find(".fp-user-search");
                            $(fp).find(".fp-date").attr("readonly", "true").datepicker({ minDate: 0 });
                            $(fp).find(".fp-time-start,.fp-time-end").attr("readonly", "true").timepicker({
                                controlType: 'select',
                                timeFormat: "HH:mm",
                                onClose: function () { search.trigger("click"); },
                                stepHour: 1,
                                stepMinute: 10,
                                hourMin: 6,
                                hourMax: 23
                            });
                        }
                    });
                }
                else {//状态列表
                    calendar = panel.uniCalendar({
                        mode: kvp.md,
                        modes: kvp.md,
                        style: kvp.style || "dft",
                        alone: kvp.alone || false,
                        operate: kvp.operate || 'drag',
                        width: width,
                        objTitleMinWidth: 100,
                        pctrl: { num: 20, triggerHeight: kvp.triggerHeight || 120 },//定义即启用
                        evSelTime: selDate,
                        dayOpt: {
                            unit: parseInt("10" || 10),
                            evSelObj: function (data) {
                                if (pro.calendar && pro.calendar.selObjFun) {//不能定义在hrload页面内
                                    pro.calendar.selObjFun(data.obj);
                                }
                            }
                        },
                        evUpTime: function (date, callback,options) {
                            var pra = kvp || {};
                            pra.date = date.format("yyyyMMdd");
                            //if (kvp.islong == "true")
                            //pra.ck_close = "true";//检查开放区间不开放日期 耗资源
                            pro.j.dev.getRsvSta(pra, function (rlt) {
                                var list = rlt.data;
                                if (list.length > 0) {
                                    if ((list[0].limit & 1024) > 0) {//预约不检测冲突
                                        options.dayOpt.occupy = false;//时间条不覆盖全部
                                    }
                                }
                                //if(list.length==0) uni.msgBox("没有获取到数据");
                                callback(list, "unilab3", { byType: kvp.byType || "lab", showClose: ("1" == "1" ? true : false) });
                            });
                        },
                        evFinishDraw: function (dt, date, opt, iqz, more) {
                            if (uni_calendar_dft_opt.finishDraw) uni_calendar_dft_opt.finishDraw(date, opt, iqz, more);
                        }
                    });
                }
            }
            //默认自动加载
            if (purl.auto_load != "false") loadCld();
            //记录对象
            if (pro.calendar) {
                if (!pro.calendar.instants) pro.calendar.instants = {};
                var cld = {};
                cld.type = purl.display;
                cld.instant = calendar;
                cld.reload = loadCld;
                pro.calendar.instants[purl.cld_name] = cld;
            }
            //点击刷新
            if (purl.display == "cld") {
                $(".resv_stat").click(function () {
                    if (calendar)
                        calendar.uploadCld();
                });
            }
        });
        function SelDateTime(data) {
            if (!pro.isloginL(function () { SelDateTime(data) })) return;
            var k = "0";//预约须知
            if (k == "" || k == "0")
                Show();
            else {
                var para = {};//通用
                var obj = data.obj;
                if (k == "2") {
                    var prefix = "";
                    var forSub = parseInt("10");
                    if (obj.clskind=="2" && (forSub & 2) > 0) prefix = "cpt";
                    else if (obj.clskind =="8" && (forSub & 8) > 0) prefix = "seat";
                    if (calendar_para.src_type == "rm") {
                        para.type = "rm_"+prefix+"rule";//房间
                        para.id = obj.roomId;
                    }
                    else if (calendar_para.src_type == "kind") {
                        para.type = "kind_" + prefix + "rule";//类型
                        para.id = obj.kindId;
                    }
                    else if (calendar_para.src_type == "dev") {
                        para.type = "dev_" + prefix + "rule";//设备
                        para.id = obj.devId;
                    }
                    else if (obj.classId) {
                        para.type = prefix+"rule";//类别
                        para.id = obj.classId;
                    }
                }
                pro.d.other.resvNotice(null, para, function (dlg) {
                    if (dlg.agree) {
                        Show();
                    }
                });
            }
            function Show() {//外层定义检查回调函数
                if (uni_calendar_dft_opt.cusPrepare) {
                    uni_calendar_dft_opt.cusPrepare(data, ShowForm);
                }
                else {
                    ShowForm(data);
                }
            }
        }
        function ShowForm(data) {
            var md = data.md;
            var obj = data.obj;
            var dlg = idlg;//$(idlg.html());
            //初始化备选项
            if ((parseInt("0" || 0) & 4) > 0) {
                pro.j.util.getCodeTbl(9, '', function (rlt) {//服务=9
                    var arr = rlt.data;
                    var str = "";
                    for (var i = 0; i < arr.length; i++) {
                        str += "<span class='spare_item'>" + arr[i].szCodeName + "</span>";
                    }
                    $(".spare_items", dlg).html(str);
                    var spare = $(".spare_item", dlg);
                    var memo = $(".spare_con", dlg);
                    spare.click(function () {
                        var pthis = $(this);
                        var v = pthis.html() + ',';
                        if (pthis.hasClass("selected")) {
                            pthis.removeClass("selected");
                            var ht = memo.val();
                            memo.val(ht.replace(v, ''));
                        }
                        else {
                            pthis.addClass("selected");
                            memo.val(v + memo.val());
                        }
                    })
                });
            }
            //初始化时间  
            obj.date = data.dt;
            if (data.startT) {
                obj.startDate = data.startD;
                obj.endDate = data.endD;
                obj.start = data.startT;
                obj.end = data.endT;
            }
            else {
                obj.start = data.start;
                obj.end = data.end;
            }
            //教师排课
            if ("0" == "1" && (parseInt(pro.acc.ident) & 512) > 0) {
                obj.cycleDate = true;
                $(".prop", dlg).val(8);//lock_room属性=8 custom
                //$(".tr_theme", dlg).removeClass("hidden");//是否需要/必须填写课题 交由resvTheme配置项确定
                //$(".con_theme", dlg).addClass("must");
                //$(".name_theme", dlg).html("<span class='red'>*</span>课程");
            }
            else
                $(".prop", dlg).val("");
            //主题显示检测
            var clsk = parseInt("1");
            if (clsk) {
                if ((clsk & (calendar_para.classkind || 0)) == 0) {
                    $(".tr_theme", dlg).addClass("hidden");
                }
            }
            //教学实验项目
            if (calendar_para.test_id && calendar_para.term) {
                $(".test_id", dlg).val(calendar_para.test_id);
                $(".term", dlg).val(calendar_para.term);
            }
            //按类型与否赋值
            var tmp = obj.id.split("_");//20150610前为&
            var id = tmp[0];
            $(".lab_id", dlg).val(tmp[1]);
            $(".type", dlg).val(obj.type || "dev");
            debugger;
            if (obj.type == "kind") {
                $(".kind_id", dlg).val(id);
                $(".room_id", dlg).val(tmp[2]||"");
            }
            else {
                $(".kind_id", dlg).val(obj.typeId);
                $(".dev_id", dlg).val(id);
            }
            //按长期与否分别初始化
            if (obj.islong) {
                //异步获取开放时间
                if (obj.type == "kind")
                    pro.j.dev.getDevKindRsvSta(id, obj.date, function (rlt) {
                        obj.open = rlt.data.open;
                        openResvDlg(dlg, obj);
                    });
                else
                    pro.j.dev.getDevRsvSta(id, obj.date, function (rlt) {
                        obj.open = rlt.data.open;
                        openResvDlg(dlg, obj);
                    });
            }
            else {
                openResvDlg(dlg, obj);
            }
            //注册提交事件
            var sub_btn = $(".mt_sub_resv", dlg);
            if (!sub_btn.hasClass("inited")) {
                sub_btn.addClass("inited");
                sub_btn.click(function () {
                    if (dlg.mustItem())
                        subUserResv(this, obj);
                });
            }
        }
        function openResvDlg(dlg, obj) {
            if (obj.islong) {
                var open = obj.open;
                if (open && open.length > 1) {
                    obj.openStart = open[0];
                    obj.openEnd = open[1];
                }
                else {
                    uni.msgBox("所选日期不开放");
                    return;
                }
            }
            //固定时间段
            if(obj.ops&&obj.ops.length>0&&(obj.ops[0].limit&2)>0){
                obj.fix = true;
                //{ };
            }
            pro.d.basic.addDateTimePicker($(".dlg_dt_panel", dlg), obj);
            //初始化状态条
            if ("1" == "1" && obj.allowLong == false) {
                $(".rsv_state_slider", dlg).stateSlider(obj, { start: $(".md_date .mt_start_time", dlg), end: $(".md_date .mt_end_time", dlg), width: 410 });
            }
            //成员添加
            if (parseInt(obj.maxUser) < 2) $(".md_group", dlg).hide();
            else {
                $(".md_group", dlg).show();
                var mb_panel = $(".dlg_mb_panel", dlg);
                if ($.trim(mb_panel.html()) == "") {
                    var para = { md: "simple" };
                    if (calendar_para.test_id) {//教学组
                        para.md = "complex";
                        para.test_id = calendar_para.test_id;
                    }
                    else {//普通组
                        if (obj.maxUser > 12) para.md = "complex";
                        para.min = obj.minUser;
                        para.max = obj.maxUser;
                    }
                    pro.d.basic.mGroupMembers(mb_panel, para);
                }
            }
            //上传文件
            if ((parseInt(obj.limit) & 8) > 0 || ("0" == "1" && (parseInt(calendar_para.classkind || 0) & 1) > 0)) //limit=8必须上传附件 研修间类型可上传
                var upFile = $(".upload_file", dlg).uploadFile();
            else
                $(".file_up_panel", dlg).hide();
            //规则详细
            $(".div_remark", dlg).html(pro.htm.getResvRule(obj));
            //参数
            $(".rsv_obj_name", dlg).html(uni.backText(obj.title));
            $(".apply_people", dlg).html(pro.acc.name);
            //打开窗口
            //$(".mt_sub_resv", dlg).removeAttr("disabled");
            uni.dlg(dlg, "预约申请", 460, 200);
        }
        //提交预约
        function subUserResv(btn, obj) {
            btn = $(btn);
            var dlg = btn.parents(".dialog:first");
            //btn.attr({ "disabled": "disabled" });
            pro.j.rsv.fRsv("set_resv", $("form:first", dlg), function () {
                if (uni_calendar_dft_opt.submitSuc) {
                    uni_calendar_dft_opt.submitSuc(dlg, obj);
                }
                else {
                    var msg = uni.translate("申请提交成功，是否跳转查看预约信息？");
                    if (parseInt(obj.minUser) > 1) {
                        msg += "<br/><br/><div style='font-weight:bold;'>" + uni.translate("注意！生效后需至少") + "<span style='color:red;font-size:bold;'>" + obj.minUser + "</span>" + uni.translate("人刷卡，否则将记为违约！") + "</div>";
                    }
                    uni.confirm(msg, function () {
                        $("#user_center").trigger("click");
                    }, function () {
                        uni.reload();
                    });
                    $(".group_id", dlg).val("");
                    $(".group_name", dlg).html("小组未创建");
                    dlg.dialog("close");
                }
                //btn.removeAttr("disabled");
            }, function (rlt) {
                uni.msgBox(rlt.msg);
                //btn.removeAttr("disabled");
            }, function () {
                uni.msgBox("异步连接出现异常！");
                //btn.removeAttr("disabled");
            });
        }
    })()
</script>
<div id="calendar_636828365424843750" name="" onselectstart="return false"></div>

                    <div class="calendar_pctrl"></div>
                </div>
                <div>
                    
                </div>
                <div>
                    <ul class="hardware clear list-paddingleft-2" style="list-style-type: none;"><p style="margin-top: 3px; margin-bottom: 3px; padding: 0px;"><span style="font-size: 20px;">房间内的配置如下：</span></p><p style="margin-top: 3px; margin-bottom: 3px; padding: 0px;"><span style="font-size: 20px;">书柜1个</span></p><p style="margin-top: 3px; margin-bottom: 3px; padding: 0px;"><span style="font-size: 20px;">桌子1张&nbsp;</span></p><p style="margin-top: 3px; margin-bottom: 3px; padding: 0px;"><span style="font-size: 20px;">2*3插座2个</span></p><p style="margin-top: 3px; margin-bottom: 3px; padding: 0px;"><span style="font-size: 20px;">椅子1把</span></p><p style="margin-top: 3px; margin-bottom: 3px; padding: 0px;"><span style="font-size: 20px;">网络接口1个</span></p></ul><p><br/></p>
                </div>
                <div>
                    <div class="img_large">
                        <img src='../../upload/info/upload/2015-07-11/mm2.130810590009390000.jpg'>  
                    </div>
                    <div class="img_thumb">
                        <ul class="clear">
                            <li><a class='cur' ><img src='../../upload/info/upload/2015-07-11/mm2.130810590009390000.jpg'></a></li>
                        </ul>
                    </div>
                    <script>
                    $(".img_thumb a").click(function () {
                        var thumbimgurl = $(this).children().attr('src');
                        var largeimagenurl = thumbimgurl.replace("", "");
                        $(".img_large img").attr('src', largeimagenurl);
                        $(".img_thumb a").each(function () {
                            if ($(this).hasClass('cur')) {
                                $(this).removeClass('cur');
                            };
                        })
                        $(this).addClass('cur');
                        return false;
                    })
                    </script>
                </div>
            </div>
        </div>
        <script>
            $(".info_unitab").unitab();
        </script>
        <script>
            function subDevResv() {
                $(".mt_sub_resv", dlg).attr({ "disabled": "disabled" });
                pro.j.rsv.fRsv("set_yard_rsv", $("form", dlg), function () {
                    uni.confirm("申请提交成功，是否跳转到个人中心？", function () {
                        $("#user_center").trigger("click");
                    }, function () {
                        uni.reload();
                    });
                    $(".mt_sub_resv", dlg).removeAttr("disabled");
                    dlg.dialog("close");
                }, function (rlt) {
                    uni.msgBox(rlt.msg);
                    $(".mt_sub_resv", dlg).removeAttr("disabled");
                }, function () {
                    uni.msgBox("异步连接出现异常！");
                    $(".mt_sub_resv", dlg).removeAttr("disabled");
                });
            }
        </script>
    </div>
</body>
</html>
{"ret":1,"act":"get_rsv_sta","msg":"ok","data":[{"id":"3676503_3674920","title":"中北校区单人间C421","name":"中北校区单人间C421","devId":"3676503","devName":"中北校区单人间C421","clskind":"1","kindId":"3675133","kindName":"中北研究室（木门）","classId":"3675132","className":"中北研究室（木门）","labName":"中北校区图书馆四楼","labId":"3674920","roomName":"中北校区单人间C421","roomId":3676502,"buildingId":0,"buildingName":"","campus":"闵行校区","islong":false,"allowLong":false,"iskind":false,"ischeck":false,"devsta":0,"runsta":65542,"state":null,"freeSta":0,"freeTime":0,"freeTbl":null,"ruleId":3685900,"rule":"&nbsp;","prop":33554433,"limit":0,"earliest":2880,"latest":0,"max":240,"min":30,"cancel":31,"maxUser":1,"minUser":1,"ext":"","open":["08:00","22:00"],"openStart":"08:00","openEnd":"22:00","clsDate":null,"ts":[{"id":null,"start":"2019-01-11 17:50","end":"2019-01-11 21:50","state":"doing","date":null,"name":null,"title":null,"owner":"马强","accno":"9822552","member":"","limit":null,"occupy":true}],"cls":[],"ops":[{"id":null,"start":"08:00","end":"22:00","state":"open","date":"2019-01-11 ","name":null,"title":null,"owner":null,"accno":null,"member":null,"limit":0,"occupy":false}]},{"id":"3676511_3674920","title":"中北校区单人间C422","name":"中北校区单人间C422","devId":"3676511","devName":"中北校区单人间C422","clskind":"1","kindId":"3675133","kindName":"中北研究室（木门）","classId":"3675132","className":"中北研究室（木门）","labName":"中北校区图书馆四楼","labId":"3674920","roomName":"中北校区单人间C422","roomId":3676510,"buildingId":0,"buildingName":"","campus":"闵行校区","islong":false,"allowLong":false,"iskind":false,"ischeck":false,"devsta":0,"runsta":65542,"state":null,"freeSta":0,"freeTime":0,"freeTbl":null,"ruleId":3685900,"rule":"&nbsp;","prop":1,"limit":0,"earliest":2880,"latest":0,"max":240,"min":30,"cancel":31,"maxUser":1,"minUser":1,"ext":"","open":["08:00","22:00"],"openStart":"08:00","openEnd":"22:00","clsDate":null,"ts":[{"id":null,"start":"2019-01-11 17:20","end":"2019-01-11 21:20","state":"doing","date":null,"name":null,"title":null,"owner":"陈正宇","accno":"9760293","member":"","limit":null,"occupy":true},{"id":null,"start":"2019-01-11 21:20","end":"2019-01-11 22:00","state":"undo","date":null,"name":null,"title":null,"owner":"曹璠","accno":"58806403","member":"","limit":null,"occupy":true}],"cls":[],"ops":[{"id":null,"start":"08:00","end":"22:00","state":"open","date":"2019-01-11 ","name":null,"title":null,"owner":null,"accno":null,"member":null,"limit":0,"occupy":false}]},{"id":"3676538_3674920","title":"中北校区单人间C425","name":"中北校区单人间C425","devId":"3676538","devName":"中北校区单人间C425","clskind":"1","kindId":"3675133","kindName":"中北研究室（木门）","classId":"3675132","className":"中北研究室（木门）","labName":"中北校区图书馆四楼","labId":"3674920","roomName":"中北校区单人间C425","roomId":3676537,"buildingId":0,"buildingName":"","campus":"闵行校区","islong":false,"allowLong":false,"iskind":false,"ischeck":false,"devsta":0,"runsta":65542,"state":null,"freeSta":0,"freeTime":0,"freeTbl":null,"ruleId":3685900,"rule":"&nbsp;","prop":1,"limit":0,"earliest":2880,"latest":0,"max":240,"min":30,"cancel":31,"maxUser":1,"minUser":1,"ext":"","open":["08:00","22:00"],"openStart":"08:00","openEnd":"22:00","clsDate":null,"ts":[{"id":null,"start":"2019-01-11 20:00","end":"2019-01-11 22:00","state":"doing","date":null,"name":null,"title":null,"owner":"黄浩","accno":"9801207","member":"","limit":null,"occupy":true}],"cls":[],"ops":[{"id":null,"start":"08:00","end":"22:00","state":"open","date":"2019-01-11 ","name":null,"title":null,"owner":null,"accno":null,"member":null,"limit":0,"occupy":false}]},{"id":"3676547_3674920","title":"中北校区单人间C426","name":"中北校区单人间C426","devId":"3676547","devName":"中北校区单人间C426","clskind":"1","kindId":"3675133","kindName":"中北研究室（木门）","classId":"3675132","className":"中北研究室（木门）","labName":"中北校区图书馆四楼","labId":"3674920","roomName":"中北校区单人间C426","roomId":3676546,"buildingId":0,"buildingName":"","campus":"闵行校区","islong":false,"allowLong":false,"iskind":false,"ischeck":false,"devsta":0,"runsta":65542,"state":null,"freeSta":0,"freeTime":0,"freeTbl":null,"ruleId":3685900,"rule":"&nbsp;","prop":1,"limit":0,"earliest":2880,"latest":0,"max":240,"min":30,"cancel":31,"maxUser":1,"minUser":1,"ext":"","open":["08:00","22:00"],"openStart":"08:00","openEnd":"22:00","clsDate":null,"ts":[{"id":null,"start":"2019-01-11 19:50","end":"2019-01-11 22:00","state":"doing","date":null,"name":null,"title":null,"owner":"钱栋炜","accno":"9823702","member":"","limit":null,"occupy":true}],"cls":[],"ops":[{"id":null,"start":"08:00","end":"22:00","state":"open","date":"2019-01-11 ","name":null,"title":null,"owner":null,"accno":null,"member":null,"limit":0,"occupy":false}]},{"id":"3676566_3674920","title":"中北校区单人间C427","name":"中北校区单人间C427","devId":"3676566","devName":"中北校区单人间C427","clskind":"1","kindId":"3675133","kindName":"中北研究室（木门）","classId":"3675132","className":"中北研究室（木门）","labName":"中北校区图书馆四楼","labId":"3674920","roomName":"中北校区单人间C427","roomId":3676565,"buildingId":0,"buildingName":"","campus":"闵行校区","islong":false,"allowLong":false,"iskind":false,"ischeck":false,"devsta":0,"runsta":65542,"state":null,"freeSta":0,"freeTime":0,"freeTbl":null,"ruleId":3685900,"rule":"&nbsp;","prop":1,"limit":0,"earliest":2880,"latest":0,"max":240,"min":30,"cancel":31,"maxUser":1,"minUser":1,"ext":"","open":["08:00","22:00"],"openStart":"08:00","openEnd":"22:00","clsDate":null,"ts":[{"id":null,"start":"2019-01-11 18:10","end":"2019-01-11 22:00","state":"doing","date":null,"name":null,"title":null,"owner":"王环","accno":"9817636","member":"","limit":null,"occupy":true}],"cls":[],"ops":[{"id":null,"start":"08:00","end":"22:00","state":"open","date":"2019-01-11 ","name":null,"title":null,"owner":null,"accno":null,"member":null,"limit":0,"occupy":false}]},{"id":"3676574_3674920","title":"中北校区单人间C428","name":"中北校区单人间C428","devId":"3676574","devName":"中北校区单人间C428","clskind":"1","kindId":"3675133","kindName":"中北研究室（木门）","classId":"3675132","className":"中北研究室（木门）","labName":"中北校区图书馆四楼","labId":"3674920","roomName":"中北校区单人间C428","roomId":3676573,"buildingId":0,"buildingName":"","campus":"闵行校区","islong":false,"allowLong":false,"iskind":false,"ischeck":false,"devsta":0,"runsta":131078,"state":null,"freeSta":0,"freeTime":0,"freeTbl":null,"ruleId":3685900,"rule":"&nbsp;","prop":33554433,"limit":0,"earliest":2880,"latest":0,"max":240,"min":30,"cancel":31,"maxUser":1,"minUser":1,"ext":"","open":["08:00","22:00"],"openStart":"08:00","openEnd":"22:00","clsDate":null,"ts":[{"id":null,"start":"2019-01-11 18:00","end":"2019-01-11 22:00","state":"doing","date":null,"name":null,"title":null,"owner":"辛明轩","accno":"9855222","member":"","limit":null,"occupy":true}],"cls":[],"ops":[{"id":null,"start":"08:00","end":"22:00","state":"open","date":"2019-01-11 ","name":null,"title":null,"owner":null,"accno":null,"member":null,"limit":0,"occupy":false}]},{"id":"3676580_3674920","title":"中北校区单人间C429","name":"中北校区单人间C429","devId":"3676580","devName":"中北校区单人间C429","clskind":"1","kindId":"3675133","kindName":"中北研究室（木门）","classId":"3675132","className":"中北研究室（木门）","labName":"中北校区图书馆四楼","labId":"3674920","roomName":"中北校区单人间C429","roomId":3676579,"buildingId":0,"buildingName":"","campus":"闵行校区","islong":false,"allowLong":false,"iskind":false,"ischeck":false,"devsta":0,"runsta":65542,"state":null,"freeSta":0,"freeTime":0,"freeTbl":null,"ruleId":3685900,"rule":"&nbsp;","prop":1,"limit":0,"earliest":2880,"latest":0,"max":240,"min":30,"cancel":31,"maxUser":1,"minUser":1,"ext":"","open":["08:00","22:00"],"openStart":"08:00","openEnd":"22:00","clsDate":null,"ts":[{"id":null,"start":"2019-01-11 18:00","end":"2019-01-11 22:00","state":"doing","date":null,"name":null,"title":null,"owner":"万月","accno":"9856906","member":"","limit":null,"occupy":true}],"cls":[],"ops":[{"id":null,"start":"08:00","end":"22:00","state":"open","date":"2019-01-11 ","name":null,"title":null,"owner":null,"accno":null,"member":null,"limit":0,"occupy":false}]},{"id":"3676515_3674920","title":"中北校区单人间C423","name":"中北校区单人间C423","devId":"3676515","devName":"中北校区单人间C423","clskind":"1","kindId":"3675133","kindName":"中北研究室（木门）","classId":"3675132","className":"中北研究室（木门）","labName":"中北校区图书馆四楼","labId":"3674920","roomName":"中北校区单人间C423","roomId":3676514,"buildingId":0,"buildingName":"","campus":"中北校区","islong":false,"allowLong":false,"iskind":false,"ischeck":false,"devsta":0,"runsta":65542,"state":null,"freeSta":0,"freeTime":0,"freeTbl":null,"ruleId":3685900,"rule":"&nbsp;","prop":33554433,"limit":0,"earliest":2880,"latest":0,"max":240,"min":30,"cancel":31,"maxUser":1,"minUser":1,"ext":"","open":["08:00","22:00"],"openStart":"08:00","openEnd":"22:00","clsDate":null,"ts":[{"id":null,"start":"2019-01-11 18:00","end":"2019-01-11 22:00","state":"doing","date":null,"name":null,"title":null,"owner":"秦乐琦","accno":"9832961","member":"","limit":null,"occupy":true}],"cls":[],"ops":[{"id":null,"start":"08:00","end":"22:00","state":"open","date":"2019-01-11 ","name":null,"title":null,"owner":null,"accno":null,"member":null,"limit":0,"occupy":false}]},{"id":"3676522_3674920","title":"中北校区单人间C424","name":"中北校区单人间C424","devId":"3676522","devName":"中北校区单人间C424","clskind":"1","kindId":"3675133","kindName":"中北研究室（木门）","classId":"3675132","className":"中北研究室（木门）","labName":"中北校区图书馆四楼","labId":"3674920","roomName":"中北校区单人间C424","roomId":3676521,"buildingId":0,"buildingName":"","campus":"中北校区","islong":false,"allowLong":false,"iskind":false,"ischeck":false,"devsta":0,"runsta":65542,"state":null,"freeSta":0,"freeTime":0,"freeTbl":null,"ruleId":3685900,"rule":"&nbsp;","prop":33554433,"limit":0,"earliest":2880,"latest":0,"max":240,"min":30,"cancel":31,"maxUser":1,"minUser":1,"ext":"","open":["08:00","22:00"],"openStart":"08:00","openEnd":"22:00","clsDate":null,"ts":[{"id":null,"start":"2019-01-11 18:00","end":"2019-01-11 22:00","state":"doing","date":null,"name":null,"title":null,"owner":"孟鑫","accno":"9802153","member":"","limit":null,"occupy":true}],"cls":[],"ops":[{"id":null,"start":"08:00","end":"22:00","state":"open","date":"2019-01-11 ","name":null,"title":null,"owner":null,"accno":null,"member":null,"limit":0,"occupy":false}]}],"ext":null}