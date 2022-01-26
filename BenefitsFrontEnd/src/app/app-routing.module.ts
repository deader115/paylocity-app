import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { PreviewCostComponent } from './components/preview-cost/preview-cost.component';
import { LookupCostComponent } from './components/lookup-cost/lookup-cost.component';

const routes: Routes = [
  { path: '', redirectTo: 'preview-cost', pathMatch: 'full' },
  { path: 'preview-cost', component: PreviewCostComponent },
  { path: 'lookup-cost', component: LookupCostComponent },
]

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
