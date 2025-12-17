// Slide content matching original 2 slides with expanded detail

export interface SlideContent {
  id: string
  type: 'definitions' | 'alignment'
  title: string
  subtitle?: string
  sections?: Section[]
  footer?: string
  sources?: Source[]
  keyInsight?: string
}

interface Section {
  heading: string
  subheading?: string
  definition?: string
  components?: string[]
  examples?: {
    correct: Example[]
    incorrect: Example[]
  }
  // For alignment slide
  items?: FlowItem[]
  guardrails?: boolean
}

interface Example {
  text: string
  note?: string
}

interface Source {
  text: string
  url: string
}

interface FlowItem {
  text: string
  type: 'strategy' | 'goal' | 'tactic' | 'result' | 'guardrail' | 'person'
  direction?: 'aligned' | 'scattered'
}

export const slides: SlideContent[] = [
  {
    id: 'slide-1-definitions',
    type: 'definitions',
    title: 'Strategy vs. Goals vs. Tactics',
    subtitle: 'Understanding the hierarchy of corporate planning',
    sections: [
      {
        heading: 'STRATEGY',
        subheading: 'Where & how to compete',
        definition: 'An integrated set of choices that uniquely position an organization to create sustainable competitive advantage—including explicit trade-offs about what NOT to do.',
        components: [
          'Where to Play: Markets, customers, geographies, product categories to pursue',
          'How to Win: Unique value proposition and competitive advantages',
          'Trade-offs: Explicit choices about what NOT to do',
          'Activity Fit: Ensure all activities reinforce each other'
        ],
        examples: {
          correct: [
            { text: '"Dominate mid-market manufacturing software through vertical specialization. We will NOT pursue enterprise accounts or horizontal applications."' },
            { text: '"Win in short-haul, point-to-point routes with no meals, no seat assignments, no hub transfers—enabling rapid turnaround and lowest costs." (Southwest Airlines)' },
            { text: '"Serve young, price-conscious furniture buyers through self-service and flat-pack design—sacrificing customers wanting delivery and assembly." (IKEA)' }
          ],
          incorrect: [
            { text: '"Be the best software company and grow revenue 20%."', note: 'No choices, no trade-offs—this is a goal, not a strategy' },
            { text: '"Delight our customers and be number one in the market."', note: 'Vague aspiration with no positioning or differentiation' },
            { text: '"Focus on innovation and quality."', note: 'No specific choices about where to compete or what to sacrifice' }
          ]
        }
      },
      {
        heading: 'GOALS',
        subheading: 'What outcomes to achieve',
        definition: 'Specific, measurable outcomes with defined timeframes that translate strategic intent into concrete targets.',
        components: [
          'Specific: Clear articulation of what success looks like',
          'Measurable: Quantifiable metrics to track progress',
          'Achievable: Realistic given available resources',
          'Relevant: Aligned with strategic objectives',
          'Time-bound: Defined deadline for achievement'
        ],
        examples: {
          correct: [
            { text: '"Acquire 500 new manufacturing customers in North America by December 2026."' },
            { text: '"Increase recurring subscription revenue to 30% of total revenue by FY2026."' },
            { text: '"Achieve #2 market share position in European market within three years."' },
            { text: '"Reduce customer acquisition cost by 25% while maintaining conversion rate by Q4 2025."' }
          ],
          incorrect: [
            { text: '"Grow market share significantly."', note: 'Vague, no metrics, no deadline—unmeasurable' },
            { text: '"Become more profitable."', note: 'No specific target or timeframe' },
            { text: '"Improve customer satisfaction."', note: 'No quantifiable metric or deadline' }
          ]
        }
      },
      {
        heading: 'TACTICS',
        subheading: 'How to execute',
        definition: 'Specific actions, initiatives, or methods employed to execute strategy and achieve goals—operational, short-term, and adjustable.',
        components: [
          'Short-term: Days to months timeframe',
          'Actionable: Concrete activities with clear steps',
          'Adjustable: Can be changed without altering strategy',
          'Owned: Clear accountability and responsibility',
          'Measurable: Trackable outputs and milestones'
        ],
        examples: {
          correct: [
            { text: '"Sponsor NAM conference; hire 3 vertical sales reps; launch LinkedIn campaign targeting plant managers."' },
            { text: '"Launch referral program offering 20% discount for new customer acquisitions."' },
            { text: '"Redesign checkout flow to reduce cart abandonment by Q2."' },
            { text: '"Run targeted LinkedIn campaign to plant operations managers in Midwest."' }
          ],
          incorrect: [
            { text: '"Do more marketing and sales."', note: 'Not actionable—no specific activity or owner' },
            { text: '"Improve our processes."', note: 'Vague—no concrete action or timeline' },
            { text: '"Be more customer-focused."', note: 'Aspirational statement, not an executable action' }
          ]
        }
      }
    ],
    keyInsight: 'Strategy defines what NOT to do • Goals are measurable targets • Tactics are swappable actions',
    sources: [
      { text: 'Porter, M. "What Is Strategy?" Harvard Business Review, 1996', url: 'https://hbr.org/1996/11/what-is-strategy' },
      { text: 'Martin, R. "The Big Lie of Strategic Planning" Harvard Business Review, 2014', url: 'https://hbr.org/2014/01/the-big-lie-of-strategic-planning' },
      { text: 'McKinsey & Company. "Strategy to beat the odds"', url: 'https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/strategy-to-beat-the-odds' }
    ]
  },
  
  {
    id: 'slide-2-alignment',
    type: 'alignment',
    title: 'Strategy Creates Alignment—Its Absence Creates Chaos',
    sections: [
      {
        heading: 'WITHOUT STRATEGY',
        subheading: 'No guardrails → scattered effort, wasted resources',
        guardrails: false,
        items: [
          { text: 'No Strategy Defined', type: 'strategy' },
          { text: '🎯 GOAL: Grow Revenue', type: 'goal' },
          { text: 'Employee A', type: 'person', direction: 'scattered' },
          { text: 'Employee B', type: 'person', direction: 'scattered' },
          { text: 'Employee C', type: 'person', direction: 'scattered' },
          { text: 'Employee D', type: 'person', direction: 'scattered' },
          { text: '"Cut all costs"', type: 'tactic' },
          { text: '"Chase enterprise"', type: 'tactic' },
          { text: '"Expand globally"', type: 'tactic' },
          { text: '"Discount heavily"', type: 'tactic' },
          { text: 'RESULT: Conflicting priorities, organizational drift', type: 'result' }
        ]
      },
      {
        heading: 'WITH STRATEGY',
        subheading: 'Clear guardrails → aligned execution, compounding advantage',
        guardrails: true,
        items: [
          { text: 'STRATEGY: Win mid-market manufacturing\nTrade-off: NOT enterprise, NOT horizontal', type: 'strategy' },
          { text: '🎯 GOAL: 500 Mfg Customers by 2026', type: 'goal' },
          { text: 'Employee A', type: 'person', direction: 'aligned' },
          { text: 'Employee B', type: 'person', direction: 'aligned' },
          { text: 'Employee C', type: 'person', direction: 'aligned' },
          { text: 'Employee D', type: 'person', direction: 'aligned' },
          { text: 'NAM sponsor', type: 'tactic' },
          { text: 'Vertical reps', type: 'tactic' },
          { text: 'Mfg LinkedIn', type: 'tactic' },
          { text: 'Case studies', type: 'tactic' },
          { text: 'RESULT: Reinforcing tactics, compounding advantage', type: 'result' }
        ]
      }
    ],
    keyInsight: '"The essence of strategy is choosing what not to do." — Michael Porter. Trade-offs create guardrails that align everyone\'s tactics toward the goal.',
    sources: [
      { text: 'Porter, M. "What Is Strategy?" Harvard Business Review, 1996', url: 'https://hbr.org/1996/11/what-is-strategy' },
      { text: 'McKinsey Quarterly. "Strategic choices that lead to results"', url: 'https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights' }
    ]
  }
]
