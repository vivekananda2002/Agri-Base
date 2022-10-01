import subprocess as sp
import pymysql
import pymysql.cursors
from tabulate import tabulate
def viewTable(rows):

    a = []
    try:
        a.append(list(rows[0].keys()))
    except:
        print("\n-----------------\nEMPTY TABLE\n-----------------\n")
        return
    for row in rows:
        b = []
        for k in row.keys():
            b.append(row[k])
        a.append(b)
    print(tabulate(a, tablefmt="psql", headers="firstrow"))
    print()
    return

def Select1():
      preq= "SELECT Crop_Name FROM CROP"
      cur.execute(preq)
      r= cur.fetchall()
      print("The available crops are:")
      viewTable(r)
      

      tmp = input('Enter the Name of the crop:')

      query = "SELECT Name, Survey_No_Range FROM CULTIVATES, FARMER WHERE Farmer_PBookNo = PBook_No AND Crop_Name = %s"  

      try:
        cur.execute(query,(tmp,))

        results = cur.fetchall()

        viewTable(results)

      except:
          print("Error:")

def Select2():
    preq= "SELECT Mach_Name FROM MACHINERY"
    cur.execute(preq)
    r= cur.fetchall()
    print("The available Machines are:")
    viewTable(r)
      


    temp = input("Enter the name of machine for which you want to know suppliers info:")
    
    query = "SELECT Name, Phone_No \
        FROM MACHINERY m, SUPPLIER  \
        WHERE m.Supplier_PhNo = Phone_No AND m.Mach_Name = '%s'" %(temp, )
    try:
     cur.execute(query)  
    
     results = cur.fetchall()

     viewTable(results)

       
   
    except:
     print("Error:")

def Select3():
    preq= "SELECT Name FROM LOCATION"
    cur.execute(preq)
    r= cur.fetchall()
    print("The available Locations are:")
    viewTable(r)
      
    inpt = input('Enter the Location_Name:')  

    query = "SELECT F.Name, F.Pbook_no \
            FROM FARMER F \
            WHERE F.Pincode IN (SELECT Pincode FROM FARMER_LOC WHERE F.Pincode = Pincode AND Location_Name = '%s') " % (inpt,)

    
    try:
     cur.execute(query)  
    
     results = cur.fetchall()
     
     viewTable(results)

       
   
    except:
     print("Error:")
  
def Select4():
    preq= "SELECT Mach_Name FROM MACHINERY"
    cur.execute(preq)
    r= cur.fetchall()
    print("The available Machines are:")
    viewTable(r)
    temp = input('Enter the name of the machine for which you need skilled labour:')

    query= "SELECT Name, Phone_No \
    FROM SKILLED_LABOUR, OPERATES \
    WHERE Phone_No = Labourer_PhNo AND Mach_Name = '%s' " % (temp,) 
    
    try:
     cur.execute(query)  
    
     results = cur.fetchall()

     viewTable(results)
       
   
    except:
     print("Error:")

def Select5():
    preq= "SELECT Name FROM WATER_RESOURCE"
    cur.execute(preq)
    r= cur.fetchall()
    print("The available water resources are:")
    viewTable(r)
       
    temp = input("Enter the name of water resource for which u want to know about farmers using them:")

    query= "SELECT Name, PBook_No \
        FROM FARMER, CULTIVATES \
        WHERE PBook_No = Farmer_PBookNo AND Water_Resource_Name = '%s'" %(temp,) 

    try:
     cur.execute(query)  
    
     results = cur.fetchall()

     viewTable(results)

    except:
     print("Error:")
 
def Select6():
    temp =input("Enter the name of machine for which u want to know the details of farmers using them")

    query = "SELECT Name, PBook_No \
        FROM PROVIDES, FARMER \
        WHERE Farmer_PBook_No = PBook_No AND MACH_NAME = '%s'" %(temp,)
    try:
     cur.execute(query)  
    
     results = cur.fetchall()

     viewTable(results)
    except:
     print("Error:")
 
def Project1(num):
   if num==1:
       print("Ascending order of crops based on water usage")
       query ="SELECT Crop_Name,Water_required_per_acre \
                FROM CROP \
                ORDER BY Water_required_per_acre"
       try:
            cur.execute(query)          
            results = cur.fetchall()
            viewTable(results)
       except:
            print("Error:")
   elif num==2:
        print("Ascending order of crops based on cost")
        query ="SELECT Crop_Name,Cost_per_acre \
                FROM CROP \
                ORDER BY Cost_per_acre "
        try:
            cur.execute(query)  
            results = cur.fetchall()
            viewTable(results)
        except:
            print("Error:")

def Project2():
    temp = int(input("Machine with rent cost greater than :"))
    query = "SELECT Mach_Name FROM MACHINERY WHERE Cost > %d " %(temp,)
   
    try:
     cur.execute(query)  
    
     results = cur.fetchall()
     
     viewTable(results)

    except:
     print("Error:")     

def Project3():
    temp = int(input("Land size:"))

    query1 = "CREATE OR REPLACE VIEW TOTAL_LAND  (Farmer_PBookNo,Total_Size) AS SELECT R.Farmer_PBookNo, SUM(L.Size) FROM CULTIVATES R, LAND L WHERE R.Survey_No_Range = L.Survey_no_range  GROUP BY R.Farmer_PBookNo"
    query2 = "SELECT Farmer_PBookNo,Total_Size FROM TOTAL_LAND WHERE Total_Size > %d" %(temp,)
   
    try:
       cur.execute(query1) 
       con.commit()     
       cur.execute(query2)
       results = cur.fetchall()

       viewTable(results)
     

    except:
       print("Error:")
 

def Project4():
    print("The water resources being over used are")

    query = "SELECT Name \
        FROM WATER_RESOURCE\
         WHERE Present_Volume < Ideal_Volume "
    try:
     cur.execute(query)  
    
     results = cur.fetchall()

     viewTable(results)

    except:
     print("Error:")

def Project5():
    temp = int(input("Input Wage (x):"))

    query = "SELECT Name, Phone_No FROM DAILY_WG_LABOUR WHERE Wage < %d" %(temp,)
    
    try:
     cur.execute(query)  
    
     results = cur.fetchall()

     viewTable(results)

    except:
     print("Error:")
def Project6():
    preq= "SELECT Utility FROM MACH_USED_FOR"
    cur.execute(preq)
    r= cur.fetchall()
    print("The utilities are:")
    viewTable(r)
    temp = input("Input required utility: ")

    query = "SELECT K.Mach_Name ,K.Supplier_PhNo, K.Cost FROM MACHINERY K, MACH_USED_FOR M WHERE K.Mach_Name = M.Mach_Name AND M.Utility = '%s'" %(temp)

    try:
        cur.execute(query)
        results = cur.fetchall()
        viewTable(results)
    
    except:
        print("Error:")


def Aggregate1():
    preq= "SELECT Name FROM LOCATION"
    cur.execute(preq)
    r= cur.fetchall()
    print("The available Locations are:")
    viewTable(r)
        
    temp = input("Name of the loc for which u need max demand crop:")

    query = "SELECT Crop_Name, Quantity \
             FROM DEMAND \
             WHERE Quantity IN (SELECT MAX(Quantity) FROM DEMAND WHERE Location_Name = '%s') AND Location_Name = '%s';" %(temp,temp,)
    try:
     cur.execute(query)  
     results = cur.fetchall()
     viewTable(results)

    except:
     print("Error:")

def Aggregate2():
    preq= "SELECT Name FROM LOCATION"
    cur.execute(preq)
    r= cur.fetchall()
    print("The available Locations are:")
    viewTable(r)
    temp =input("Enter the name of location for which u need total prod of all crops:")
     
    query = "SELECT C.Crop_Name, SUM(L.Size)*C.Yield_per_acre \
            FROM CULTIVATES R, LAND L, CROP C WHERE Location_Name = '%s'\
             AND R.Survey_No_Range = L.Survey_no_range AND R.Crop_Name = C.Crop_Name GROUP BY C.Crop_Name" %(temp,)
    try:
     cur.execute(query)  
    
     results = cur.fetchall()

     viewTable(results)

    except:
     print("Error:")


      
def Search(num):
    if num == 1 :
        temp = input("Name of Farmer:")
        query= "SELECT * FROM FARMER WHERE Name = '%s' " %(temp,)
        try:
           cur.execute(query)  
           results = cur.fetchall()
           viewTable(results)

        except:
            print("Error:")
    if num==2 :
        temp = input("Name of Labourer:")
        query= "SELECT * FROM LABOURER WHERE Labourer_Name = '%s' " %(temp,)
        try:
           cur.execute(query)  
           results = cur.fetchall()
           viewTable(results)

        except:
            print("Error:")
    
    if num==3 :
        temp = input("Name of WaterResource:")
        query= "SELECT * FROM WATER_RESOURCE WHERE Name = '%s' " %(temp,)
        try:
           cur.execute(query)  
           results = cur.fetchall()
           viewTable(results)

        except:
            print("Error:")
    
    if num==4 :
        temp = input("Name of crop:")
        query= "SELECT * FROM CROP WHERE Crop_Name = '%s' " %(temp,)
        try:
           cur.execute(query)  
           results = cur.fetchall()
           viewTable(results)

        except:
            print("Error:")
    if num==5:
        preq= "SELECT Mach_Name FROM MACHINERY"
        cur.execute(preq)
        r= cur.fetchall()
        print("The available Machines are:")
        viewTable(r)

        temp = input("Name of Machine_Name:")
        query= "SELECT * FROM MACHINERY WHERE Mach_Name = '%s'" %(temp,)
        try:
           cur.execute(query)  
           results = cur.fetchall()
           viewTable(results)

        except:
            print("Error:")

    if num==6:
        temp = input("Input SurveyNo:")
        query= "SELECT Name, PBook_No \
               FROM FARMER, CULTIVATES \
               WHERE Farmer_PBook_No = PBook_No AND Survey_No_Range = '%s' " %(temp,)
        try:
           cur.execute(query)  
           results = cur.fetchall()
           viewTable(results)
        except:
            print("Error:")

def Analysis1():
   print("The Details of machinery and crop inputs which have demand greater than half of farmers")
 
   query1 = "SELECT COUNT(PBook_No) FROM FARMER"
   query2 = "SELECT Mach_Name, COUNT(Farmer_PBook_No) FROM PROVIDES GROUP BY Mach_Name"
   query3 = " SELECT U.Crop_Input_Name, COUNT(C.Farmer_PBookNo) FROM USED_ON U, CULTIVATES C WHERE U.Survey_No_Range = C.Survey_No_Range GROUP BY U.Crop_Input_Name"
   try : 
       cur.execute(query1)
       results = cur.fetchall()
       tcnt=results[0]['COUNT(PBook_No)']
       
       cur.execute(query2)
       results = cur.fetchall()
       print("List of machines")
       for row in results:
           if row['COUNT(Farmer_PBook_No)']>=tcnt:
               print(row['Mach_Name'])
       
       cur.execute(query3)
       results = cur.fetchall()
       print("List of crop inputs")
       for row in results:
           if row['COUNT(Farmer_PBook_No)']>=tcnt:
               print(row['Crop_Input_Name'])
       
         

   except:
        print("Error:")


def Analysis2():
   print("Farmers with access to multiple water resources and using an overused water resource ")
   query1 ="SELECT COUNT(Water_Resource_Name),Farmer_PBookNo FROM CULTIVATES GROUP BY Farmer_PBookNo "
   query2 = "SELECT Water_Resource_Name, Farmer_PBookNo FROM WATER_RESOURCE, CULTIVATES WHERE Ideal_Volume > Present_Volume AND Name = Water_Resource_Name"
     
   try:
        cur.execute(query1)
        result1 = cur.fetchall()
        cur.execute(query2)
        result2 = cur.fetchall()
      
        for rows1 in result1:
          for rows2 in result2:
              if rows1['Farmer_PBookNo']==rows2['Farmer_PBookNo']:
                  print(rows1['Farmer_PBookNo']) 
                   
   except:
          print("Error:")
     

def Analysis3():
    temp=input("Name of the location for which info of Crops that are being over produced or under produced is needed:")
    query1= "SELECT C.Crop_Name, SUM(L.Size)*C.Yield_per_acre \
             FROM CULTIVATES R, LAND L, CROP C WHERE Location_Name = '%s'\
             AND R.Survey_No_Range = L.Survey_no_range AND R.Crop_Name = C.Crop_Name GROUP BY C.Crop_Name" %(temp,)
    
    query2="SELECT Crop_Name,Quantity FROM DEMAND WHERE Location_Name = '%s'" % (temp,)
    try:
      cur.execute(query1)
      results1= cur.fetchall()
      #viewTable(results1)
      
      cur.execute(query2)
      results2 = cur.fetchall()
      #viewTable(results2)
      
      for row1 in results1:
          for row2 in results2:
                if row1['Crop_Name']==row2['Crop_Name'] :
                   print('Crop:', row1['Crop_Name'] ,'Production: ',row1['SUM(L.Size)*C.Yield_per_acre'] ,' Demand: ' ,row2['Quantity'])

    
    except:
       print("Error:") 
     

def Modification1(num):
   if num==1:
        print("Updating work status of labourer:")
        temp1 = input("Phone number:")
        try:        
            query1="UPDATE LABOURER SET Work_Status = '0' ,Farmer_Pbook_No= NULL  WHERE Phone_No = '%s' OR Leader_PhNo='%s'" %(temp1,temp1)
            cur.execute(query1)
            con.commit()
        except Exception as e:
            con.rollback()
            print("Failed")
            print(">>>>>>>>>>>>>", e)

   elif num ==2:
        print("Update wage") 
        temp1 = input("Phone number:")
        temp2 = int(input("New Wage:" ))
        try:
            query="SELECT Wage_type FROM LABOURER WHERE Phone_No = '%s'"%(temp1)
            cur.execute(query)
            wgtype = cur.fetchone()
        except Exception as e:
                con.rollback()
                print("Failed")
                print(">>>>>>>>>>>>>", e)
        if wgtype["Wage_type"]=='Daily':
            try:
                q1="UPDATE DAILY_WG_LABOUR SET Wage = '%d' WHERE Phone_No = '%s'"%(temp2,temp1)
                cur.execute(q1)
                con.commit()
                print("Wage updated succesfully")
            except Exception as e:
                con.rollback()
                print("Failed ")
                print(">>>>>>>>>>>>>", e)
        elif wgtype["Wage_type"]=='Work_based':
            try:
                q2="UPDATE WORK_BASED_LABOUR SET Cost_Per_Acre = '%d' WHERE Phone_No = '%s'"%(temp2,temp1)
                cur.execute(q2)
                con.commit()
                print("Wage updated succesfully")
            except Exception as e:
                con.rollback()
                print("Failed ")
                print(">>>>>>>>>>>>>", e)

           
    
 

def Modification2():
    print("Update crop grown")
    temp1= input("Survey_no  chars:")
    temp2=input("New Crop Name:")
    temp3 = input("Sart date YYYY-MM-DD: ")
    query1="UPDATE CULTIVATES SET Crop_Name = '%s' WHERE Survey_No_Range = '%s' "%(temp2,temp1,)
    query2="UPDATE CULT_DETAILS SET Start_Date = '%s' WHERE Survey_No_Range = '%s' " %(temp3,temp1,)
    try:
        cur.execute(query1)
        con.commit()
        cur.execute(query2)
        con.commit()


    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)


def Modification3(num):
  if num==1:
        print("Adding a new machine:")
        try:
            row={}
            row[0] = input("Name of the machine:")
            row[1] = input("Supplier Phone Number:")
            row[2] = int(input("Rent Cost:"))
            row[3] = int(input("Purchse_Cost:"))
            query="INSERT INTO MACHINERY VALUES('%s','%s','%d','%d');" % (row[0],row[1],row[2],row[3],)
            cur.execute(query)
            con.commit()
            print("Machine added succesfully")
        except:
            con.rollback()
            print("Failed")
            print(">>>>>>")	
  elif num==2:
        print("Delete Machine:")
        try:
            row={}
            row[0]= input("Name of the machine:")
            row[1]= input("Supplier Phone number:")
            query = "DELETE FROM MACHINERY WHERE Mach_Name='%s' AND Supplier_PhNo = '%s'" %(row[0],row[1])
            cur.execute(query)
            con.commit()
            print("Machine Deleted Succesfully")
        except:
            con.rollback()
            print("Failed")
            print(">>>>>>")
  elif num ==3:
        print("Update Rent Cost")
        try:
            row={}
            row[0]= input("Name of the machine:")
            row[1]= input("Supplier Phone number:")
            row[2] = int(input("New Rent Cost:"))
            query= "UPDATE MACHINERY SET Cost='%d' WHERE Mach_Name='%s' AND Supplier_PhNo = '%s'"%(row[2],row[0],row[1])
            cur.execute(query)
            con.commit()
            print("Rent cost updated Succesfully")
        except:
            con.rollback()
            print("Failed")
            print(">>>>>>")            

def Modification4():
    try:
        print("Land owner updation ")
        row ={}
        row[0] = input("Survey number of the land :")
        row[1] = input("New Owner pass book number :")
        query="UPDATE CULTIVATES SET Farmer_PBookNo = '%s' WHERE Survey_No_Range = '%s'" %(row[1],row[0])
        cur.execute(query)
        con.commit()
    except Exception as exp:
        con.rollback()
        print("Failed")
        print(">>>>>>",exp)	                      

def Modification5(num):
    if num ==1:
      try:
        print("For Deletion of Farmer ")
        row={}
        row[0] = input("Pass book number :")
        query = "DELETE FROM FARMER WHERE Pbook_No = '%s'" %(row[0])
        cur.execute(query)
        con.commit()
        print("Succesfully Deleted")
      except Exception as exp:
        con.rollback()
        print("Failed")
        print(">>>>>>",exp)	
    if num == 2:
      try:
        print("For Deletion of Labourer ")
        row={}
        row[0] = input("Phone number  :")
        query = "DELETE FROM LABOURER WHERE Phone_No = '%s' " %(row[0])
        cur.execute(query)
        con.commit()
        print("Succesfully Deleted")
      except Exception as exp:
        con.rollback()
        print("Failed")
        print(">>>>>>",exp) 
   

def Modification7():
    try:
        print("Updating MSP of acrop")
        row={}
        row[0]=input("Name of the crop:")
        row[1] = input("MSP:")
        query="UPDATE CROP SET MSP = '%d' WHERE Crop_Name = '%s' "%(row[1],row[0])
        cur.execute(query)
        con.commit()
    except Exception as exp:	
	    con.rollback()
	    print("Failed")
	    print(">>>>>>",exp)

def hire_a_labour():
    temp1 = input("Enter your Pass book number:")
    temp2 = input("Labour phone number:")

    try:
        check1 ="Select Work_Status FROM LABOURER WHERE Phone_No = '%s'" %(temp2)
        cur.execute(check1) 
        ch = cur.fetchall
        if ch==1:
            print("Labourer Not Available")
        else:
            try:
                query="UPDATE LABOURER SET Work_Status = 1 ,Farmer_Pbook_No ='%s' WHERE Phone_No = '%s' OR Leader_PhNo='%s' "%(temp1,temp2,temp2)
                cur.execute(query)
                con.commit()
                print("Hired Labourer Succesfully")
            except Exception as exp:	
	            con.rollback()
	            print("Failed")
	            print(">>>>>>",exp)
    except Exception as exp:	
	        con.rollback()
	        print("Failed")
	        print(">>>>>>",exp)

def InsertSupplier():
   try:
     row = {}  

     print("Enter SUPPLIER details:")  
     row["Name"] = input("Supplier's Name:")  
     row["Father_Name"] = input("Father's Name:")  
     row["Phone_No"] = input("Phone number:")
     if len(row["Phone_No"])!=10 :
      print("Phone number should be of 10 digits")
      return  
     query = "INSERT INTO SUPPLIER(Name, Father_Name, Phone_No) VALUES('%s','%s','%s')" % (row["Name"], row["Father_Name"], row["Phone_No"]) 
     print(query)  
     cur.execute(query)  
     con.commit()  
     print("Inserted Into Database")   

   except Exception as e:  
     con.rollback()   
     print("Failed to insert into database")  
     print(">>>>>>>>>>",e)   

   return

def InsertDependent():
   try:  
     row = {} 

     print("Enter Dependent details:") 

     row["Dependent_Name"] = input("Dependents Name : ") 

     row["Age"] = int(input("Age :")) 

     row["Relation"] = input("Relation with the farmer:") 

     row["Pbook_no"] = input("Passbook number of the farmer :") 
    
     if len(row["Pbook_no"])!=14 :
        print("Pass book number should be of 14 characters")
        return

     query = "INSERT INTO DEPENDENT (Dependent_Name, Age, Relation, Pbook_no)  VALUES('%s', '%d', '%s', '%s')" % (row["Dependent_Name"], row["Age"], row["Relation"] , row["Pbook_no"])
     cur.execute(query) 
     con.commit() 
     print("Inserted Into Database") 

   except Exception as e : 
        con.rollback() 
        print("Failed to insert into database") 
        print(">>>>>>>>>>",e) 

   return  


def Insertlabourer():
 try: 
    row = {} 
    print("Enter new Labourer's details: ") 
    row["Labourer_Name"] = input("Name : ") 
    row["Labourer_fathername"] = input("Father's Name: ") 
    phno = input("Phone number: ") 

    if(len(phno) != 10): 
      print("Invalid input for Mobile no.") 
      return 

    row["Phone_no"] = phno 

    se = int(input("Skill exist (1/0): ")) 
    if se ==0 :
        row["Age"] = int(input("Age in yrs:"))

    if se not in (0,1) : 
        print("Invalid input for Skill exist") 
        return   

    row["Skill_exist"] = bool(se) 


    ws = int(input("Work status (1/0): ")) 

    if ws not in (0,1): 
     print("Invalid input for Work status") 
     return 

    row["Work_Status"] = bool(ws) 
    row["Wage_type"] = input("Type of wage (Daily/Work_based): ")
    row["Wage"]=int(input("Wage:"))
    if ws == 1:
     row["Farmer_Pbook_No"] = input("Pass Book number of the farmer currently using services: ") 

    row["Location_Name"]=input("Name of the location currently residing in: ") 
    lphno = input("Phone number of the Leader: ") 
    
    if(len(phno) != 10): 
         print("Invalid phone number") 
         return 

    row["Leader_PhNo"]= lphno 
    if ws ==1:
      query = "INSERT INTO LABOURER(Labourer_Name,Labourer_fathername,Phone_No,Skill_exist,Work_Status,Wage_type,Farmer_PBook_No,Location_Name,Leader_PhNo) VALUES('%s', '%s', '%s', '%d', '%d', '%s', '%s', '%s','%s')" % (row["Labourer_Name"], row["Labourer_fathername"], row["Phone_no"], row["Skill_exist"], row["Work_Status"], row["Wage_type"], row["Farmer_Pbook_No"], row["Location_Name"], row["Leader_PhNo"])
    else:
     query = "INSERT INTO LABOURER(Labourer_Name,Labourer_fathername,Phone_No,Skill_exist,Work_Status,Wage_type,Farmer_PBook_No,Location_Name,Leader_PhNo) VALUES('%s', '%s', '%s', '%d', '%d', '%s', NULL, '%s','%s')" % (row["Labourer_Name"], row["Labourer_fathername"], row["Phone_no"], row["Skill_exist"], row["Work_Status"], row["Wage_type"], row["Location_Name"], row["Leader_PhNo"])
    cur.execute(query)
    con.commit()
    if se == 1 :
         q= "INSERT INTO SKILLED_LABOUR VALUES('%s','%s')" % (row["Labourer_Name"],row["Phone_no"])
         cur.execute(q)
         con.commit()
    elif se ==2 :
         q= "INSERT INTO UNSKILLED_LABOUR VALUES('%s','%s','%d')" % (row["Labourer_Name"],row["Phone_no"],row["Age"])
         cur.execute(q)
         con.commit()
    if row["Wage_type"]=="Daily":
         q = "INSERT INTO DAILY_WG_LABOUR VALUES('%s','%s','%d')"%(row["Labourer_Name"],row["Phone_no"],row["Wage"])
         cur.execute(q)
         con.commit()
    elif row["Wage_type"]=="Work_based":
         q = "INSERT INTO DAILY_WG_LABOUR VALUES('%s','%s','%d')"%(row["Labourer_Name"],row["Phone_no"],row["Wage"])
         cur.execute(q)
         con.commit()

    print("Inserted Into Database")

 except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
 

def InsertFarmer():
  
    try:
        row = {}
        print("Enter new Farmer details: ")

        row["Name"] = input("Name : ")
        row["Father_Name"] = input("Father's Name: ")
        row["Pbook_no"] = input("Passbook number: ")
        if len(row["Pbook_no"])!=14:
            print("Passbook number should be of 14 chars")
            return
        row["Phno"] = input("Mobile number: ")
        if len(row["Phno"])!=10:
            print("Phone number should be of 10 digits")
            return
        row["Sex"] = input("Sex (Male/Female/Other): ")
        row["Street_Village"] = input("Street name & Village name: ")
        row["District_State"] = input("Dustrict name & State name: ")
        row["DOB"]=input("Date of Birth (YYYY-MM-DD): ")
        row["Acc_no"]=input("Bank Acc no:")
        
        preq= "SELECT IFSC FROM BANK_DETAILS"
        cur.execute(preq)
        r= cur.fetchall()
        print("The Banks are:")
        viewTable(r)
        row["IFSC"]=input("IFSC code:")
        
        if len(row["IFSC"])!=11:
            print("IFSC should be of 11 chars")
            return
        preq= "SELECT Pincode FROM FARMER_LOC"
        cur.execute(preq)
        r= cur.fetchall()
        print("The pincodes are:")
        viewTable(r)
        row["Pincode"]=input("Pincode :")
        if len(row["Pincode"])!=6:
            print("Pincode should be of 6 digits")
            return

        query = "INSERT INTO FARMER(Name,Father_Name,Pbook_no,Phno,Sex,Street_Village,District_State,DOB,Acc_no,IFSC,Pincode) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s','%s')" % (
            row["Name"], row["Father_Name"], row["Pbook_no"], row["Phno"], row["Sex"], row["Street_Village"], row["District_State"], row["DOB"], row["Acc_no"],row["IFSC"],row["Pincode"])

        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def dispatch_far():
  while(1):
        input("Enter any key to CONTINUE>")
        print("1.Suppliers of machine       2.Skill based labour search   3.Crops order by cost")
        print("4.Hire Labourer(s)           5.Machine with utility        6.Wage based (<x) Labour Search")
        print("7.Tot crop production in loc 8.Crops order by water usage  9.Search Labourer")
        print("10.Details of crop           11.Details of machine         12.Update crop grown on")
        print("13.Add new Dependent         14.Exit    ")

        t = int(input("Enter the option:"))
        sp.call('clear', shell=True)
        if t==1 :
            Select2()
        elif t==2:
            Select4()
        elif t==3:
            Project1(2)
        elif t==4:
            hire_a_labour()
        elif t==5:
            Project6()
        elif t==6:
            Project5
        elif t==7:
            Aggregate2()
        elif t==8:
            Project1(1)
        elif t==9:
            Search(2)
        elif t==10:
            Search(4)
        elif t==11:
            Search(5)
        elif t==12:
            Modification2()
        elif t==13:
            InsertDependent()
        elif t==14:
            break
        else:
            print("Error: Invalid option")

def dispatch_govt():
  while(1):
        input("Enter any key to CONTINUE>")
        print(" 1.Crop based farmer search    2.Farmers in alocation     3.Farmers using a water source")
        print(" 4.Crops order by water usage  5.Crops order by cost      6.Farmers with land greater than:")
        print(" 7.Overused water sources      8.Max demand crop in aloc  9.Tot production in a loc")
        print("10.Search Farmer              11.Search water source     12.Search Land")
        print("13.Faremer reqs Analysis      14.Water source Analysis   15.Crop production Analysis")
        print("16.Update land owner          17.Delete Farmer           18.Delete Labourer")
        print("19.Update MSP                 20.Insert Farmer           21.Insert Supplier")
        print("22.Insert Labourer            23.Exit")

        t = int(input("Enter the option:"))
        sp.call('clear', shell=True)
        if t==1 :
            Select1()
        elif t==2:
            Select3()
        elif t==3:
            Select5()
        elif t==4:
            Project1(1)
        elif t==5:
            Project1(2)
        elif t==6:
            Project3()
        elif t==7:
            Project4()
        elif t==8:
            Aggregate1()
        elif t==9:
            Aggregate2()
        elif t==10:
            Search(1)
        elif t==11:
            Search(3)
        elif t==12:
            Search(6)
        elif t==13:
            Analysis1()
        elif t==14:
            Analysis2()
        elif t==15:
            Analysis3()
        elif t==16:
            Modification4()
        elif t==17:
            Modification5(1)
        elif t==18:
            Modification5(2)    
        elif t==19:
            Modification7()
        elif t==20:
            InsertFarmer()
        elif t==21:
            InsertSupplier()
        elif t==22:
            Insertlabourer()
        elif t==23:
            break                                                                                    
        else:
            print("Error: Invalid option")

def dispatch_sup():
 while(1):
    input("Enter any key to CONTINUE>")
    print("1.Add new Machine    2.Delete Machine    3.Update Rent cost")
    print("4.Exit ")
    t=int(input("Enter the option:"))
    sp.call('clear', shell=True)

    if t==1:
        Modification3(1)
    elif t==2:
        Modification3(2)
    elif t==3:
        Modification3(3)
    elif t==4:
        break
    else:
        print("Error: Invalid option")    


def dispatch_lab():
 while(1):
    print("1.Change work status   2.Update wage   3.Exit")
    t=int(input("Enter the option:"))

    if t==1:
        Modification1(1)
    elif t==2:
        Modification1(2)
    elif t==3:
        break
    else:
        print("Error: Invalid option")    


def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        dispatch_govt()
    elif(ch == 2):
        dispatch_far()
    elif(ch == 3):
        dispatch_sup()
    elif(ch == 4):
        dispatch_lab()
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)
    
     
    host = input("Host:")
    port = int(input("Port:"))
    user = input("Username:")
    password = input("Password: ")
     
    a =0
    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host=host,
                              port =port,
                              user=user,
                              password=password,
                              db='agri',
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                # Here taking example of Employee Mini-world
                print("1. Govt_Official")  # Hire an Employee
                print("2. Farmer")  # Fire an Employee
                print("3. Supplier")  # Promote Employee
                print("4. Labourer")  # Employee Statistics
                print("5. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 5:
                    con.close
                    a=1
                    break
                else:
                     dispatch(ch)
                     tmp = input("Enter any key to CONTINUE>")
            
            if a==1:
               break
    
    except:
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
