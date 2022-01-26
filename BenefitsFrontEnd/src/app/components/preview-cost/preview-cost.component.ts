import { Component, OnInit } from '@angular/core';
import { FormArray, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Cost } from 'src/app/models/cost.model';
import { Employee } from 'src/app/models/employee.model';
import { BenefitsService } from 'src/app/services/benefits.service';

@Component({
  selector: 'app-preview-cost',
  templateUrl: './preview-cost.component.html',
  styleUrls: ['./preview-cost.component.css']
})
export class PreviewCostComponent implements OnInit{

  employee: Employee = {
    firstName: '',
    lastName: '',
    dependents: []
  }

  cost: Cost;
  employeeForm: FormGroup;

  get dependents(): FormArray {
    return this.employeeForm.get('dependents') as FormArray;
  }

  constructor(private fb: FormBuilder, private benefitsService: BenefitsService) { }

  ngOnInit(): void {
    this.employeeForm = this.fb.group({
      firstName: ['', Validators.required],
      middleName: [''],
      lastName: ['', Validators.required],
      dependents: this.fb.array([this.buildDependentFormGroup()])
    })
  }

  buildDependentFormGroup(): FormGroup {
    return this.fb.group({
      depFirstName: ['', Validators.required],
      depMiddleName: [''],
      depLastName: ['', Validators.required],
    });
  }
  
  getCostPreview(employee: Employee): void {
    this.benefitsService.previewCost(employee).subscribe({
      next: (response: Cost) => {
        console.log(response);
        this.cost = response;
      },
      error: (ex) => console.error(ex)
    })
  }
  
  onSubmit(): void {
    console.log(this.employeeForm.value);
    this.getCostPreview(this.employeeForm.value);
  }

  addDependent() {
    this.dependents.push(this.buildDependentFormGroup());
  }

}
