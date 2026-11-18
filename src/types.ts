export interface Country {
  code: string;
  name: string;
  flag: string;
  currency: string;
  symbol: string;
}

export interface PlanPrice {
  country_code: string;
  country_name: string;
  flag: string;
  currency: string;
  symbol: string;
  original_price: number;
  converted_price_usd: number;
  target_price: number;
  target_currency: string;
  discount_percent: number;
  payment_difficulty: 'easy' | 'medium' | 'hard';
  payment_notes: string;
  price_history: number[];
  status?: 'available' | 'not_available' | 'global_usd' | 'suspended';
  status_label?: string;
  incl_tax?: boolean;
  source?: 'official' | 'store' | 'usd_flat' | 'community' | 'archive' | 'estimated' | string;
  source_url?: string;
  source_date?: string;
  fetched_at?: string;
  needs_review?: boolean;
  available?: boolean;
}

export interface ServicePlan {
  id: string;
  name: string;
  period: string;
  description: string;
  prices: PlanPrice[];
}

export interface ServiceSummary {
  id: string;
  name: string;
  slug: string;
  category: string;
  icon: string;
  color: string;
  description: string;
  default_plan_name: string;
  cheapest_country: string;
  cheapest_flag: string;
  cheapest_price_usd: number;
  cheapest_price: number;
  cheapest_currency: string;
  us_price_usd: number;
  us_price: number;
  max_discount: number;
  countries_count: number;
  available_plans: string[];
  popularity_rank: number;
}

export interface ServiceDetail extends ServiceSummary {
  official_url: string;
  guide: string;
  plans: ServicePlan[];
}

export interface MatrixRow {
  service_id: string;
  service_name: string;
  category: string;
  icon: string;
  prices: Record<string, number>;
  statuses: Record<string, string>;
  sources?: Record<string, string>;
  availables?: Record<string, boolean>;
  best_country: string;
  max_discount: number;
}

export interface CurrencyInfo {
  code: string;
  symbol: string;
  rate_usd: number;
}
