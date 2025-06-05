import { Routes } from '@angular/router';
import { HomePage } from './pages/home/home.page';
import { ProductGridComponent } from './components/product-grid/product-grid.component';
import { AccountPage } from './pages/account/account.page';

export const routes: Routes = [
    {
        path: '',
        component: HomePage,
        children: [
            {
                path: '/product',
                component: ProductGridComponent
            },
            {
                path: '/account',
                component: AccountPage
            }
        ]
    }

];
