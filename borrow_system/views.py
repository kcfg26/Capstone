from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Equipment, BorrowRecord
from datetime import date

# View to display all available equipment
def equipment_list(request):
    equipment = Equipment.objects.filter(available=True)
    return render(request, 'borrow_system/equipment_list.html', {'equipment': equipment})

# View to handle borrowing equipment
def borrow_equipment(request, equipment_id):
    equipment = Equipment.objects.get(id=equipment_id)
    if equipment.available:
        # Create a new BorrowRecord
        BorrowRecord.objects.create(
            equipment=equipment,
            borrowed_by=request.user.username,  # Or use the actual user data if applicable
            borrow_date=date.today()
        )
        # Mark the equipment as unavailable
        equipment.available = False
        equipment.save()
        return redirect('equipment_list')  # Redirect to equipment list after borrowing
    else:
        return HttpResponse("This equipment is currently unavailable.", status=400)

# View to handle returning equipment
def return_equipment(request, borrow_id):
    borrow_record = BorrowRecord.objects.get(id=borrow_id)
    borrow_record.return_date = date.today()
    borrow_record.save()

    # Make the equipment available again
    equipment = borrow_record.equipment
    equipment.available = True
    equipment.save()

    return redirect('equipment_list')  # Redirect to equipment list after returning
