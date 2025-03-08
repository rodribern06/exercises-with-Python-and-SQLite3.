import pandas as pd
import matplotlib.pyplot as plt
import sqlite3 
with sqlite3.connect('database/northwin.db') as conn:#obteniendo empleados y productos mas rentables
    query = '''
        SELECT ProductName, ROUND(SUM(Price * Quantity)) as sumatot
        FROM OrderDetails od
        JOIN Products p ON p.productID = od.ProductID
        GROUP BY od.ProductID
        ORDER BY sumatot DESC
        LIMIT 10
    '''
    top_products = pd.read_sql_query(query,conn)
    top_products.plot(x='ProductName',y='sumatot',kind='bar',figsize=(10,5),legend=False)
    
    plt.title('productos mas rentables')
    plt.xlabel('productos')
    plt.ylabel('revenue')
    plt.grid()
    plt.xticks(rotation=90)
    plt.show()
    
    query2 = '''
        SELECT FirstName, COUNT(*) AS totalV
        FROM ORDERS o
        JOIN Employees e ON o.EmployeeID = e.EmployeeID
        GROUP by e.EmployeeID
        ORDER by TotalV ASC
        LIMIT 3
    '''
    total_vents = pd.read_sql_query(query2,conn)
    total_vents.plot(x='FirstName',y='totalV',kind='bar',figsize=(10,5),legend=False)
    plt.xlabel('empleado')
    plt.ylabel('ventas')
    plt.title('efectividad de ventas')
    plt.xticks(rotation=90)
    plt.show()
     
    query3= """
          SELECT FirstName,sum(ValorOrden) as TotVent
          FROM Profit
          GROUP BY FirstName
          ORDER BY ToTVent ASC
    """
    total_ventasprice=pd.read_sql_query(query3,conn)
    total_ventasprice.plot(x='FirstName',y='TotVent',kind='bar',figsize=(8,4),legend=False)
    plt.title('top sellers')
    plt.xlabel('Employees')
    plt.ylabel('Revenue')
    plt.xticks(rotation=45)
    plt.show()
    