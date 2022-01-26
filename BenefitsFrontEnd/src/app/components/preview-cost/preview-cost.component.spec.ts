import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PreviewCostComponent } from './preview-cost.component';

describe('PreviewCostComponent', () => {
  let component: PreviewCostComponent;
  let fixture: ComponentFixture<PreviewCostComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PreviewCostComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PreviewCostComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
