#!/usr/bin/env node

import { Command } from 'commander';
import chalk from 'chalk';
import { initCommand } from '../src/commands/init.js';
import { researchCommand } from '../src/commands/research.js';
import { planCommand } from '../src/commands/plan.js';
import { statusCommand } from '../src/commands/status.js';
import { metricsCommand } from '../src/commands/metrics.js';
import { verifyCommand } from '../src/commands/verify.js';

const program = new Command();

program
  .name('drewsky')
  .description(chalk.blue('drewsky AI collaboration framework - Research → Plan → Implement'))
  .version('0.1.0');

program
  .command('init [project-name]')
  .description('Initialize drewsky framework in a project')
  .action(initCommand);

program
  .command('research <task>')
  .description('Create research document with TCREI validation')
  .action(researchCommand);

program
  .command('plan')
  .option('--from-research', 'Generate plan from existing research')
  .description('Generate implementation plan with Task/Progress Ledgers')
  .action(planCommand);

program
  .command('status')
  .description('Show current workflow state')
  .action(statusCommand);

program
  .command('metrics')
  .description('Show productivity and token savings stats')
  .action(metricsCommand);

program
  .command('verify')
  .option('--file <path>', 'Specific file to verify (default: .research.md or .plan.md)')
  .description('Run Chain of Verification on file claims')
  .action(verifyCommand);

program.parse(process.argv);
