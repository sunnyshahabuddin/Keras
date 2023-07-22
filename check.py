// dashboard.component.ts
import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {
  data: any[] = [];

  constructor(private http: HttpClient) { }

  getData() {
    const apiUrl = 'http://localhost:3000/api/dashboard';

    this.http.get<any[]>(apiUrl).subscribe(
      (response) => {
        this.data = response;
        console.log('Data from API:', this.data);
      },
      (error) => {
        console.error('Error fetching data:', error);
      }
    );
  }
}
