import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { User } from '../../models/user.interface';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../../services/api.service';

@Component({
    selector: 'product-grid',
    standalone: true,
    imports: [CommonModule, FormsModule],
    templateUrl: 'product-grid.component.html',
    // styleUrl: 'product-grid.component.css',
})

export class ProductGridComponent {
    inputUsername: string = '';
    userData: User | null = null;
    loading: boolean = false;
    error: string | null = null;

    constructor (private apiService: ApiService) {}

    fetchUser() {
        this.apiService.getUser(this.inputUsername).subscribe({
            next: (data) => {
                this.userData = data;
            },
            error: (error) => {
                console.error('Error:', error);
                this.error = 'User not found or error occurred';
                this.loading = false;
            }
        });
    }
}