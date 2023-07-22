import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {
  data: any[] = [];

  constructor(private http: HttpClient) {}

  getData(): void {
    this.getDataFromApi().subscribe((result: any) => {
      this.data = result;
    });
  }

  getDataFromApi(): Observable<any> {
    const apiUrl = 'http://localhost:3000/api/dashboard';
    return this.http.get(apiUrl);
  }
}
