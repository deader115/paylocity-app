import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

// TODO: Reconfigure URLs for better organization
const baseUrl = 'http://localhost:8000';

@Injectable({
  providedIn: 'root'
})
export class BenefitsService {

  constructor(private http: HttpClient) { }

  // TODO: Properly type employeeData
  previewCost(employeeData: any) {
    return this.http.post(baseUrl + '/preview-cost', JSON.stringify(employeeData), {headers: {'Content-Type': 'application/json'}, withCredentials: true})
  }

  lookupCost(id: number) {
    return this.http.get(`${baseUrl}/lookup-cost/${id}`)
  }
}
