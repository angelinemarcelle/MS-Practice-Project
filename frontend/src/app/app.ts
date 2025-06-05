import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { HomePage } from './pages/home/home.page';
import { RouterOutlet } from '@angular/router';
import 'zone.js';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, HomePage, RouterOutlet],
  templateUrl: './app.html',
  // styleUrl: './app.css',
  // template: `<router-outlet></router-outlet>`
})

export class App{
  protected title = 'heavenlyvitamin';
}
