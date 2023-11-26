import { NgModule } from '@angular/core';
import {
  NbFormFieldModule, NbButtonModule, NbCardModule, NbCheckboxModule, NbDatepickerModule, NbIconModule, NbInputModule, NbMenuModule,
   NbRadioModule,
  NbSelectModule, 
  NbWindowModule} from '@nebular/theme';

import { ThemeModule } from '../@theme/theme.module';
import { PagesComponent } from './pages.component';
import { DashboardModule } from './dashboard/dashboard.module';
import { ECommerceModule } from './e-commerce/e-commerce.module';
import { PagesRoutingModule } from './pages-routing.module';
import { MiscellaneousModule } from './miscellaneous/miscellaneous.module';
import { IcfesDashboardComponent } from './icfes-dashboard/icfes-dashboard.component';

@NgModule({
  imports: [
    PagesRoutingModule,
    ThemeModule,
    NbMenuModule,
    DashboardModule,
    ECommerceModule,
    MiscellaneousModule,
    NbButtonModule,
    NbInputModule,
    NbCardModule,
    NbCheckboxModule,
    NbRadioModule,
    NbDatepickerModule,
    NbSelectModule,
    NbIconModule,
    NbFormFieldModule,
    NbWindowModule.forChild(),
  ],
  declarations: [
    PagesComponent,
    IcfesDashboardComponent,
  ],
})
export class PagesModule {
}