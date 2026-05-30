import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit {
  title = 'frontend';
  apiResponse: any = null;

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.http.get('http://127.0.0.1:8000/').subscribe({
      next: (data) => {
        this.apiResponse = data;
        console.log('--- MONOREPO CONNECTIVITY CHECK ---');
        console.log('Backend & Database status:', data);
      },
      error: (err) => {
        console.error('Failed to connect to backend API:', err);
      }
    });
  }
}
