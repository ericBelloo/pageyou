from django.shortcuts import render

# Create your views here.
import csv, pyexcel

"""
    def process_cps(request, file_name):
    if file_name:
        path_file = 'static/catalogs/%s.csv' % file_name

        with open(path_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='|', quotechar="'")
            for row in csv_reader:
                cp_string = str(row[0])
                colony = str(row[1])
                city = str(row[2])
                state = str(row[3])

                # Estado Objeto
                state_object, created_state = State.objects.get_or_create(name=state)

                # Ciudad objeto
                city_object, created_city = City.objects.get_or_create(name=city, state_id=state_object.id)

                # Objeto CP
                if len(cp_string) <= 4:
                    cp_string = '0%s' % cp_string
                cp_object, created_cp = CP.objects.get_or_create(
                    id=cp_string,
                    city=city_object,
                    state=state_object
                )

                # Ahora la colonia
                Colony.objects.get_or_create(
                    cp=cp_object,
                    city=city_object,
                    name=colony
                )

        csv_file.close()

    return HttpResponse('Process')

"""