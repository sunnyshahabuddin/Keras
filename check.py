import { Component, OnInit } from '@angular/core';
import { Chart, Point } from 'chart.js';

@Component({
  selector: 'app-infocus',
  templateUrl: './infocus.component.html',
  styleUrls: ['./infocus.component.css']
})
export class InfocusComponent implements OnInit {

  ngOnInit(): void {
    this.createLineChart();
  }

  createLineChart() {
    const ctx = (document.getElementById('lineChart') as HTMLCanvasElement).getContext('2d');
    const chart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: ['January 2023', 'February 2023'],
        datasets: [{
          label: 'Infocus Data',
          data: [
            { x: 'January 2023', y: 1.73 },
            { x: 'February 2023', y: 1.68 }
          ],
          borderColor: 'red',
          fill: false
        }]
      },
      options: {
        scales: {
          x: {
            type: 'time',
            time: {
              unit: 'month',
              displayFormats: {
                month: 'MMM YYYY'
              }
            },
            ticks: {
              source: 'labels'
            }
          },
          y: {
            ticks: [1.67, 1.68, 1.69, 1.70, 1.71, 1.72, 1.73]
          }
        },
        plugins: {
          legend: {
            display: true,
            position: 'top'
          }
        }
      }
    });
  }
}
