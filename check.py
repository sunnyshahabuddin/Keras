import { Component, AfterViewInit } from '@angular/core';
import { Chart, LineController, LineElement, PointElement, LinearScale, CategoryScale, Tooltip } from 'chart.js';

@Component({
  selector: 'app-infocus',
  templateUrl: './infocus.component.html',
  styleUrls: ['./infocus.component.css']
})
export class InfocusComponent implements AfterViewInit {

  ngAfterViewInit() {
    this.createLineChart();
  }

  createLineChart() {
    Chart.register(LineController, LineElement, PointElement, LinearScale, CategoryScale, Tooltip);

    const ctx = document.getElementById('lineChart') as HTMLCanvasElement;
    const lineChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: ['January 2023', 'February 2023'],
        datasets: [
          {
            label: 'Infocus Line Chart',
            data: [1.73, 1.68],
            borderColor: 'red',
            fill: false,
          }
        ]
      },
      options: {
        scales: {
          y: {
            beginAtZero: false,
            ticks: {
              stepSize: 0.01,
              precision: 2,
              min: 1.67,
              max: 1.73
            }
          }
        }
      }
    });
  }

}
