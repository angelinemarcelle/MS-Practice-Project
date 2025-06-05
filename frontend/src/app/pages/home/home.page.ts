
import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { ProductGridComponent } from '../../components/product-grid/product-grid.component';
import { AccountPage } from '../account/account.page';

@Component({
    selector: 'home-page',
    standalone: true,
    imports: [CommonModule, ProductGridComponent, AccountPage],
    templateUrl: './home.page.html',
})

export class HomePage {
    constructor(private router: Router) {}
    navigateToHome() {
        this.router.navigate(['/']);
    }

    navigateToAccount() {
        this.router.navigate(['/account']);
    }
}