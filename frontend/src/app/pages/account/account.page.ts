import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { User } from '../../models/user.interface';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../../services/api.service';

@Component({
    selector: 'account-page',
    standalone: true,
    imports: [CommonModule, FormsModule],
    templateUrl: './account.page.html',
})

export class AccountPage {
    inputUsername: string = '';
    inputEmail: string = ';'
    userData: User | null = null;
    loading: boolean = false;
    error: string | null = null;

    constructor (private apiService: ApiService) {}

    validateUserCredentials() {
        if (!this.inputUsername || !this.inputEmail) {
            this.error = 'Please enter both username and email';
            return;
        }

        this.loading = true;
        this.error = null;

        this.apiService.validateCredentials(this.inputUsername, this.inputEmail).subscribe({
            next: (data) => {
                this.userData = data;
                this.loading = false;
            },
            error: (error) => {
                this.error = 'Invalid username or email combination';
                this.loading = false;
                console.error('Validation error:', error);
            }
        });
    }
}