package dbtaobao;

import java.sql.*;
import java.util.ArrayList;

/**
 * @Author: yanzx
 * @Date: 2022/6/13 11:34
 * @Description:
 */


public class connDb {
    private static Connection con = null;
    private static Statement stmt = null;
    private static ResultSet rs = null;

    //连接数据库方法
    public static void startConn() {
        try {
            Class.forName("com.mysql.jdbc.Driver");
//连接数据库中间件
            try {
                con = DriverManager.getConnection("jdbc:MySQL://192.168.26.128:3306/dbtaobao?serverTimezone=GMT%2B8&characterEncoding=utf8&useSSL=false", "root", "hadoop");
                System.out.println("连接成功!!!");
            } catch (SQLException e) {
                e.printStackTrace();
            }
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

    //关闭连接数据库方法
    public static void endConn() throws SQLException {
        if (con != null) {
            con.close();
            con = null;
        }

        if (rs != null) {
            rs.close();
            rs = null;
        }
        if (stmt != null) {
            stmt.close();
            stmt = null;
        }
    }

    //数据库双 11 所有买家消费行为比例
    public static ArrayList index() throws SQLException {
        ArrayList<String[]> list = new ArrayList();
        startConn();
        stmt = con.createStatement();
//        rs = stmt.executeQuery("select action,count(*) num from result1 group by action desc");
        rs = stmt.executeQuery("select * from result1");
        while (rs.next()) {
            String[] temp = {rs.getString("action"), rs.getString("num")};
            list.add(temp);
        }
        endConn();
        return list;
    }

    //男女买家交易对比
    public static ArrayList index_1() throws SQLException {
        ArrayList<String[]> list = new ArrayList();
        startConn();
        stmt = con.createStatement();
//        rs = stmt.executeQuery("select gender,count(*) num from result2 group by gender desc");
        rs = stmt.executeQuery("select * from result2");
        while (rs.next()) {
            String[] temp = {rs.getString("gender"), rs.getString("num")};
            list.add(temp);
        }
        endConn();
        return list;
    }

    //男女买家各个年龄段交易对比
    public static ArrayList index_2() throws SQLException {
        ArrayList<String[]> list = new ArrayList();
        startConn();
        stmt = con.createStatement();
//        rs = stmt.executeQuery("select gender,age_range,count(*) num from user_log group by gender,age_range desc");
        rs = stmt.executeQuery("select * from result3");
        while (rs.next()) {
            String[] temp = {rs.getString("gender"), rs.getString("age_range"), rs.getString("num")};
            list.add(temp);
        }
        endConn();
        return list;
    }

    //获取销量前五的商品类别
    public static ArrayList index_3() throws SQLException {
        ArrayList<String[]> list = new ArrayList();
        startConn();
        stmt = con.createStatement();
        rs = stmt.executeQuery("select * from result4");
        while (rs.next()) {
            String[] temp = {rs.getString("cat_id"), rs.getString("num")};
            list.add(temp);
        }
        endConn();
        return list;
    }

    //各个省份的的总成交量对比
    public static ArrayList index_4() throws SQLException {
        ArrayList<String[]> list = new ArrayList();
        startConn();
        stmt = con.createStatement();
        rs = stmt.executeQuery("select * from result5");
        while (rs.next()) {
            String pro = rs.getString("province");
            String[] temp = {getPro(pro), rs.getString("num")};
            list.add(temp);

        }
        endConn();
        return list;
    }

    public static String getPro(String pro) {
        switch (pro) {
            case "重庆市":
                pro = "重庆";
                break;
            case "北京市":
                pro = "北京";
            break;
            case "天津市":
                pro = "天津";
                break;
            case "上海市":
                pro = "上海";
                break;
            default:
                break;
        }
        return pro;
    }

    public static void main(String[] args) throws SQLException {
        connDb.startConn();
//        ArrayList arrayList1 = connDb.index_1();
        ArrayList arrayList2 = connDb.index_2();
//        ArrayList arrayList3 = connDb.index_3();
//        ArrayList arrayList4 = connDb.index_4();
//        ArrayList arrayList = connDb.index();
        System.out.println(arrayList2);

    }
}

