

def htmlc(ht):
    f = open("E:/class.html", 'w')
    message = """
           <h1>CLASS</h1>
           <!DOCTYPE html>
           <html>
           <head>
           <title></title>
           </head>
           <body bgcolor="">

           <table border="1">
            <tr>
            <th>__day__</th>
            <th>__period__</th>
            <th>__room_id__</th>

            <th>_n_teach_</th>
            <th>subject</th>

            </tr>
            """
    # < td > __n_id__ < / td >
    # < td > _hour_ < / td >
    # < td > _code_ < / td >
    f.write(message)


    for a in ht:
       print("working")
       f.write("<tr><td>" + str(a[4]) + "</td><td>" + str(a[0]) + "</td><td>" + a[1] + "</td><td>" + a[2] + "</td><td>" + a[3] + "</td></tr>")# <td>" +str(i[0]) + "</td><td>" + str(i[4]) + "</td><td>"+str(i[5])+"</td>

    message = """</table>
            </body>
            </html>"""
    f.write(message)
    f.close()

def htmlt(ht):
    f = open("E:/teacher.html", 'w')
    message = """
           <h1>TEACHER</h1>
           <!DOCTYPE html>
           <html>
           <head>
           <title></title>
           </head>
           <body bgcolor="">

           <table border="1">
            <tr>
              <th>__day__</th>
            <th>__period__</th>
            <th>__room_id__</th>

            <th>_n_teach_</th>
            <th>subject</th>

            </tr>
            """
    # < td > __n_id__ < / td >
    # < td > _hour_ < / td >
    # < td > _code_ < / td >
    f.write(message)


    for a in ht:
       print("working")
       f.write("<tr><td>" + str(a[4]) + "</td><td>" + str(a[0]) + "</td><td>" + a[1] + "</td><td>" + a[2] + "</td><td>" + a[3] + "</td></tr>")# <td>" +str(i[0]) + "</td><td>" + str(i[4]) + "</td><td>"+str(i[5])+"</td>

    message = """</table>
            </body>
            </html>"""
    f.write(message)
    f.close()

def viewsub(ht):
    f = open("E:/viewsub.html", 'w')
    message = """
           <h1>entered subject</h1>
           <!DOCTYPE html>
           <html>
           <head>
           <title></title>
           </head>
           <body bgcolor="">

           <table border="1">
            <tr>

            <th>_sub_id_</th>
            <th>_subject_name_</th>



            </tr>
            """
    # < td > __n_id__ < / td >
    # < td > _hour_ < / td >
    # < td > _code_ < / td >
    f.write(message)


    for a in ht:
       #print("working")
       f.write("<tr><td>" + str(a[0]) + "</td><td>" + a[1] + "</td></tr>")# <td>" +str(i[0]) + "</td><td>" + str(i[4]) + "</td><td>"+str(i[5])+"</td>

    message = """</table>
            </body>
            </html>"""
    f.write(message)
    f.close()
def viewtea(ht):
    f = open("E:/viewtea.html", 'w')
    message = """
           <h1>entered teacher</h1>
           <!DOCTYPE html>
           <html>
           <head>
           <title></title>
           </head>
           <body bgcolor="">

           <table border="1">
            <tr>

            <th>_teacher_id_</th>
            <th>_teacher_name_</th>



            </tr>
            """
    # < td > __n_id__ < / td >
    # < td > _hour_ < / td >
    # < td > _code_ < / td >
    f.write(message)


    for a in ht:
       #print("working")
       f.write("<tr><td>" + str(a[0]) + "</td><td>" + a[1] + "</td></tr>")# <td>" +str(i[0]) + "</td><td>" + str(i[4]) + "</td><td>"+str(i[5])+"</td>

    message = """</table>
            </body>
            </html>"""
    f.write(message)
    f.close()
def viewrom(ht):
    f = open("E:/viewrom.html", 'w')
    message = """
           <h1>entered room</h1>
           <!DOCTYPE html>
           <html>
           <head>
           <title></title>
           </head>
           <body bgcolor="">

           <table border="1">
            <tr>

            <th>_room_id_</th>
            <th>_room_name_</th>



            </tr>
            """
    # < td > __n_id__ < / td >
    # < td > _hour_ < / td >
    # < td > _code_ < / td >
    f.write(message)


    for a in ht:
       #print("working")
       f.write("<tr><td>" + str(a[0]) + "</td><td>" + a[1] + "</td></tr>")# <td>" +str(i[0]) + "</td><td>" + str(i[4]) + "</td><td>"+str(i[5])+"</td>

    message = """</table>
            </body>
            </html>"""
    f.write(message)
    f.close()
def viewdata(ht):
    f = open("E:/viewdata.html", 'w')
    message = """
           <h1>entered data by teacher</h1>
           <!DOCTYPE html>
           <html>
           <head>
           <title></title>
           </head>
           <body bgcolor="">

           <table border="1">
            <tr>

            <th>_teacher name_</th>
            <th>_room_name_</th>
            <th>_subject_</th>
             <th>_hour_per_week_</th>



            </tr>
            """
    # < td > __n_id__ < / td >
    # < td > _hour_ < / td >
    # < td > _code_ < / td >
    f.write(message)


    for a in ht:
       #print("working")
       f.write("<tr><td>" + a[1] + "</td><td>" + a[2] + "</td><td>" + a[4] + "</td><td>" + str(a[5]) + "</td></tr>")# <td>" +str(i[0]) + "</td><td>" + str(i[4]) + "</td><td>"+str(i[5])+"</td>

    message = """</table>
            </body>
            </html>"""
    f.write(message)
    f.close()
def viewad(ht):
    f = open("E:/viewad.html", 'w')
    message = """
           <h1>admin database</h1>
           <!DOCTYPE html>
           <html>
           <head>
           <title></title>
           </head>
           <body bgcolor="">

           <table border="1">
            <tr>

            <th>_id_</th>
            <th>_usernmae_</th>
            <th>_password_</th>



            </tr>
            """
    # < td > __n_id__ < / td >
    # < td > _hour_ < / td >
    # < td > _code_ < / td >
    f.write(message)


    for a in ht:
       #print("working")
       f.write("<tr><td>" + str(a[0]) + "</td><td>" + a[1] + "</td><td>" + a[2] + "</td></tr>")# <td>" +str(i[0]) + "</td><td>" + str(i[4]) + "</td><td>"+str(i[5])+"</td>

    message = """</table>
            </body>
            </html>"""
    f.write(message)
    f.close()
def viewout(ht):
    f = open("E:/viewout.html", 'w')
    message = """
           <h1>outdata database</h1>
           <!DOCTYPE html>
           <html>
           <head>
           <title></title>
           </head>
           <body bgcolor="">

           <table border="1">
            <tr>
            <th>_id_</th>
            <th>_day_</th>
            <th>_period_</th>
            <th>_room_</th>
             <th>_teacher_</th>
             <th>_n_teach_</th>
             <th>_subject_</th>

            </tr>
            """
    # < td > __n_id__ < / td >
    # < td > _hour_ < / td >
    # < td > _code_ < / td >
    f.write(message)


    for a in ht:
       #print("working")
       f.write("<tr><td>" + str(a[0]) + "</td><td>" + str(a[6]) + "</td><td>" + str(a[1]) + "</td><td>" + str(a[2]) + "</td><td>" + str(a[3]) + "</td><td>" + str(a[4]) + "</td><td>" + str(a[5]) + "</td></tr>")# <td>" +str(i[0]) + "</td><td>" + str(i[4]) + "</td><td>"+str(i[5])+"</td>

    message = """</table>
            </body>
            </html>"""
    f.write(message)
    f.close()