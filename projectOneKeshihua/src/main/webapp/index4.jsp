<%--
  Created by IntelliJ IDEA.
  User: 20924
  Date: 2022/6/14
  Time: 8:35
  To change this template use File | Settings | File Templates.
--%>
<%@ page language="java" import="dbtaobao.connDb,java.util.*" contentType="text/html;
charset=UTF-8"
         pageEncoding="UTF-8" %>
<%
    ArrayList<String[]> list = connDb.index_4();
    List<Integer> dataList = new ArrayList<Integer>();
    String ldata = "[";
    for (String[] data : list) {
//System.out.println(data[0]);
//System.out.println(data[1]);
        ldata += "{name:'" + data[0] + "',value:" + data[1] + "},";
        dataList.add(Integer.valueOf(data[1]));
    }
    ldata += "]";
    int min = Collections.min(dataList);
    int max = Collections.max(dataList);
%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>ECharts 可视化分析淘宝双 11</title>
    <link href="./css/style.css" type='text/css' rel="stylesheet"/>
    <script src="./js/echarts.min.js"></script>
    <script src="./js/china.js"></script>
</head>
<body>
<div class='header'>
    <p>ECharts 可视化分析淘宝双 11</p>
</div>
<div class="content">
    <div class="nav">
        <ul>
            <li><a href="./index.jsp">所有买家各消费行为对比</a></li>
            <li><a href="./index1.jsp">男女买家交易对比</a></li>
            <li><a href="./index2.jsp">男女买家各个年龄段交易对比</a></li>
            <li><a href="./index3.jsp">商品类别交易额对比</a></li>
            <li class="current"><a href="#">各省份的总成交量对比</a></li>
        </ul>
    </div>
    <div class="container">
        <div class="title">各省份的总成交量对比</div>
        <div class="show">
            <div class='chart-type'>地图</div>
            <div id="main" style="width: 1000px;height:600px;"></div>
        </div>
    </div>
</div>
<script>
    function randomData() {
        return Math.round(Math.random() * 500);
    }

    var mydata = [
        {name: '北京', value: '100'}, {name: '天津', value: randomData()},
        {name: '上海', value: randomData()}, {name: '重庆', value: randomData()},
        {name: '河北', value: randomData()}, {name: '河南', value: randomData()},
        {name: '云南', value: randomData()}, {name: '辽宁', value: randomData()},
        {name: '黑龙江', value: randomData()}, {name: '湖南', value: randomData()},
        {name: '安徽', value: randomData()}, {name: '山东', value: randomData()},
        {name: '新疆', value: randomData()}, {name: '江苏', value: randomData()},
        {name: '浙江', value: randomData()}, {name: '江西', value: randomData()},
        {name: '湖北', value: randomData()}, {name: '广西', value: randomData()},
        {name: '甘肃', value: randomData()}, {name: '山西', value: randomData()},
        {name: '内蒙古', value: randomData()}, {name: '陕西', value: randomData()},
        {name: '吉林', value: randomData()}, {name: '福建', value: randomData()},
        {name: '贵州', value: randomData()}, {name: '广东', value: randomData()},
        {name: '青海', value: randomData()}, {name: '西藏', value: randomData()},
        {name: '四川', value: randomData()}, {name: '宁夏', value: randomData()},
        {name: '海南', value: randomData()}, {name: '台湾', value: randomData()},
        {name: '香港', value: randomData()}, {name: '澳门', value: randomData()}
    ];
    mydata = <%=ldata%>
        min = <%=min%>
            max = <%=max%>
                console.log(mydata)
    var optionMap = {
        backgroundColor: '#FFFFFF',
        title: {
            text: '各省份的总成交量对比',
            subtext: '',
            x: 'center'
        },
        tooltip: {
            trigger: 'item'
        },
//左侧小导航图标
        visualMap: {
            show: true,
            x: 'left',
            y: 'center',
//splitList: [
// {start: 14800, end:15000},{start: 14700, end:14800},
// {start: 14600, end: 14700},{start: 14500, end: 14600},
// {start: 14400, end: 14500},{start: 14300, end: 14400},
//],
            min: min,
            max: max,
            inRange: {
                color: ['lightskyblue', 'yellow', 'orangered', "red"]
            },
// color: ['#5475f5', '#9feaa5', '#85daef','#74e2ca', '#e6ac53', '#9fb5ea']
        },
//配置属性
        series: [{
            name: '数据',
            type: 'map',
            mapType: 'china',
            roam: true,
            label: {
                normal: {
                    show: true //省份名称
                },
                emphasis: {
                    show: true//false
                }
            },
            data: mydata //数据
        }]
    };
    //初始化 echarts 实例
    var myChart = echarts.init(document.getElementById(
        'main'));
    //使用制定的配置项和数据显示图表
    myChart.setOption(optionMap);
</script>
</body>
</html>