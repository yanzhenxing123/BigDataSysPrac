<%@ page language="java" import="dbtaobao.connDb,java.util.*" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8"%>
<%
    ArrayList<String[]> list = connDb.index();
%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>ECharts 可视化分析淘宝双11</title>
    <link href="./css/style.css" type='text/css' rel="stylesheet"/>
    <script src="./js/echarts.min.js"></script>
</head>
<body>
<div class='header'>
    <p>ECharts 可视化分析淘宝双11</p>
</div>
<div class="content">
    <div class="nav">main
        <ul>
            <li class="current"><a href="#">所有买家各消费行为对比</a></li>
            <li><a href="./index1.jsp">男女买家交易对比</a></li>
            <li><a href="./index2.jsp">男女买家各个年龄段交易对比</a></li>
            <li><a href="./index3.jsp">商品类别交易额对比</a></li>
            <li><a href="./index4.jsp">各省份的总成交量对比</a></li>
        </ul>
    </div>
    <div class="container">
        <div class="title">所有买家各消费行为对比</div>
        <div class="show">
            <div class='chart-type'>饼图</div>
            <div id="main"></div>
        </div>
    </div>
</div>
<script>
    //基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('main'));
    // 指定图表的配置项和数据
    option = {
        backgroundColor: '#2c343c',
        title: {
            text: '所有买家消费行为比例图',
            left: 'center',
            top: 20,
            textStyle: {
                color: '#ccc'
            }
        },
        //工具提示
        tooltip : {
            //触发     项目
            trigger: 'item',
            //格式化程序
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        //直观图
        visualMap: {
            show: false,
            min: 80,
            max: 600,
            inRange: {
                colorLightness: [0, 1]
            }
        },
        //系列
        series : [
            {
                name:'消费行为',
                type:'pie',
                //半径
                radius : '55%',
                center: ['50%', '50%'],
                data:[
                    {value:<%=list.get(0)[1]%>, name:'特别关注'},
                    {value:<%=list.get(1)[1]%>, name:'购买'},
                    {value:<%=list.get(2)[1]%>, name:'添加购物车'},
                    {value:<%=list.get(3)[1]%>, name:'点击'},
                    //分类
                ].sort(function (a, b) { return a.value - b.value}),
                //玫瑰型     角
                roseType: 'angle',
                label: {
                    //正常的
                    normal: {
                        textStyle: {
                            color: 'rgba(255, 255, 255, 0.3)'
                        }
                    }
                },
                labelLine: {
                    normal: {
                        lineStyle: {
                            color: 'rgba(255, 255, 255, 0.3)'
                        },
                        smooth: 0.2,
                        length: 10,
                        length2: 20
                    }
                },
                itemStyle: {
                    normal: {
                        color: '#c23531',
                        //阴影模糊
                        shadowBlur: 200,
                        //阴影颜色
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                },
                //动画类型       规模
                animationType: 'scale',
                //动画				弹出
                animationEasing: 'elasticOut',
                //动画延迟
                animationDelay: function (idx) {
                    return Math.random() * 200;
                }
            }
        ]
    };
    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
</script>
</body>
</html>