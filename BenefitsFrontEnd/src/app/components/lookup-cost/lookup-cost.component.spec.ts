import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LookupCostComponent } from './lookup-cost.component';

describe('LookupCostComponent', () => {
  let component: LookupCostComponent;
  let fixture: ComponentFixture<LookupCostComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LookupCostComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LookupCostComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
